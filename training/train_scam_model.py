import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# -------------------------
# Load SMS Dataset
# -------------------------
sms = pd.read_csv("data/sms_spam.csv", encoding="latin-1")

# Keep only required columns
sms = sms[["v1", "v2"]]

# Rename columns
sms.columns = ["label", "text"]

# Convert labels
sms["label"] = sms["label"].map({
    "spam": 1,
    "ham": 0
})

# -------------------------
# Load Email Dataset
# -------------------------
emails = pd.read_csv("data/emails_spam.csv", encoding="latin-1")

emails = emails[["text", "spam"]]

emails.columns = ["text", "label"]

# Ensure labels are integers
emails["label"] = emails["label"].astype(int)

# -------------------------
# Merge datasets
# -------------------------
data = pd.concat([sms, emails], ignore_index=True)

# Remove missing values
data = data.dropna()

# Remove duplicates
data = data.drop_duplicates()

print("Total samples:", len(data))

# -------------------------
# Split data
# -------------------------
X = data["text"]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------
# Build model
# -------------------------
model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Train
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, pred))

print("\nClassification Report")
print(classification_report(y_test, pred))

# -------------------------
# Save Model
# -------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/scam_detector.pkl")

print("\nModel saved successfully!")