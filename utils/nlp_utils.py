import joblib

# Load the trained model
model = joblib.load("models/scam_detector.pkl")


def detect_scam_type(message):
    message = message.lower()

    if any(word in message for word in ["otp", "verification code"]):
        return "OTP Scam"

    elif any(word in message for word in ["bank", "account", "kyc", "credit card", "debit card"]):
        return "Bank Fraud"

    elif any(word in message for word in ["upi", "gpay", "phonepe", "paytm"]):
        return "UPI Fraud"

    elif any(word in message for word in ["lottery", "won", "winner", "prize", "gift"]):
        return "Lottery Scam"

    elif any(word in message for word in ["police", "cbi", "ed", "customs", "digital arrest"]):
        return "Digital Arrest Scam"

    elif any(word in message for word in ["click", "link", "http", "www"]):
        return "Phishing Scam"

    else:
        return "General Scam"


def explain_prediction(message):
    explanation = []

    keywords = [
        "urgent",
        "click",
        "verify",
        "otp",
        "bank",
        "won",
        "gift",
        "free",
        "limited",
        "account",
        "link",
        "prize"
    ]

    for word in keywords:
        if word in message.lower():
            explanation.append(word)

    if explanation:
        return "Detected suspicious words: " + ", ".join(explanation)

    return "No major suspicious keywords detected."


def predict_message(message):

    prediction = model.predict([message])[0]

    probability = model.predict_proba([message]).max()

    label = "Scam" if prediction == 1 else "Genuine"

    scam_type = detect_scam_type(message) if prediction == 1 else "None"

    explanation = explain_prediction(message)

    return {
        "label": label,
        "risk": round(probability * 100, 2),
        "type": scam_type,
        "explanation": explanation
    }