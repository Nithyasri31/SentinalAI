import os
import re
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# --------------------------------------------------
# Text Cleaning Function
# --------------------------------------------------
def clean_text(text):
    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove punctuation and special characters
    text = re.sub(r"[^a-z0-9 ]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# --------------------------------------------------
# Load SMS Dataset
# --------------------------------------------------
sms = pd.read_csv("data/sms_spam.csv", encoding="latin-1")

sms = sms[["v1", "v2"]]
sms.columns = ["label", "text"]

sms["label"] = sms["label"].map({
    "spam": 1,
    "ham": 0
})

# --------------------------------------------------
# Load Email Dataset
# --------------------------------------------------
emails = pd.read_csv("data/emails_spam.csv", encoding="latin-1")

emails = emails[["text", "spam"]]
emails.columns = ["text", "label"]

emails["label"] = emails["label"].astype(int)

# --------------------------------------------------
# Merge Datasets
# --------------------------------------------------
data = pd.concat([sms, emails], ignore_index=True)

data = data.dropna()
data = data.drop_duplicates()

# Clean text
data["text"] = data["text"].apply(clean_text)

# Shuffle dataset
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

print("Total Samples:", len(data))

# --------------------------------------------------
# Split Dataset
# --------------------------------------------------
X = data["text"]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# --------------------------------------------------
# Build Pipeline
# --------------------------------------------------
model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            stop_words="english",
            lowercase=True,
            strip_accents="unicode",
            ngram_range=(1, 2),
            min_df=2,
            max_df=0.95
        )
    ),
    (
        "classifier",
        LogisticRegression(
            solver="liblinear",
            class_weight="balanced",
            random_state=42,
            max_iter=2000
        )
    )
])

# --------------------------------------------------
# Train
# --------------------------------------------------
model.fit(X_train, y_train)

# --------------------------------------------------
# Evaluate
# --------------------------------------------------
predictions = model.predict(X_test)

print("\nAccuracy:", round(accuracy_score(y_test, predictions), 4))

print("\nClassification Report")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))

# --------------------------------------------------
# Save Model
# --------------------------------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/scam_detector.pkl")

print("\nModel saved successfully!")

# --------------------------------------------------
# Sample Predictions
# --------------------------------------------------
print("\n================ SAMPLE TESTS ================\n")

sample_messages = [
    "Congratulations! You have won ₹5,00,000. Click here to claim your prize.",
    "URGENT! Verify your OTP immediately.",
    "Your SBI KYC has expired. Update now.",
    "Hi, I'll reach home by 7 PM.",
    "Meeting is postponed to tomorrow.",
    "Claim your free iPhone now.",
    "You have won 150000"
]

for msg in sample_messages:

    prediction = model.predict([msg])[0]

    probability = model.predict_proba([msg])[0][1]

    print("-" * 70)
    print("Message :", msg)
    print("Prediction :", "Scam" if prediction == 1 else "Genuine")
    print("Scam Probability :", round(probability * 100, 2), "%")