import joblib

# Load saved model and vectorizer
model = joblib.load("intent_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Predict the intent from input text
def predict_intent(text):
    X = vectorizer.transform([text])
    return model.predict(X)[0]
