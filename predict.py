import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_news(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    return "Real" if prediction == 1 else "Fake"
