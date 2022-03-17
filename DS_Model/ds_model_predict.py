import os
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import pandas as pd

try:
    df = pd.read_csv("messages_group_db.csv", sep="\t")
    df.sort_values(by='label', ascending=True, inplace=True)
    df.reset_index(inplace=True, drop=True)
    df = df.iloc[len(df['label'])-df[df['label']==1].count().values[0]*2:,:]

    def predict_label(msg):
        X = df['message']
        tfidf = TfidfVectorizer(max_features=10000, ngram_range=(1,2))
        X = tfidf.fit_transform(X)

        vec = tfidf.transform([msg])
        clf = pickle.load(open(f"{os.getcwd()}//DS_Model//trained_model.clf", "rb"))

        return int(clf.predict(vec))
except:
    def predict_label(msg):
        return None
    pass