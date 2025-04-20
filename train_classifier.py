import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load intents
with open("intents.json") as f:
    intents = json.load(f)

# Prepare training data
texts = []
labels = []
for item in intents:
    for example in item["examples"]:
        texts.append(example)
        labels.append(item["intent"])

# Vectorize
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train classifier
model = LogisticRegression()
model.fit(X, labels)

# Save model + vectorizer
joblib.dump(model, "intent_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model trained and saved!")
