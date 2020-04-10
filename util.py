import pickle
import json
from sklearn.feature_extraction.text import TfidfVectorizer

with open("./models/model_vectorizer.pickle",'rb') as f:
    vectorizer = pickle.load(f)


with open("./models/sentiment_classifier.pkl",'rb') as f:
    loaded_clf = pickle.load(f)

#print("Loaded model")
def get_sentiment(review):
    sentiment = loaded_clf.predict(vectorizer.transform([review]))
    return sentiment[0]

