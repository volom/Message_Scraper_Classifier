from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
import pandas as pd
import os
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import warnings
warnings.filterwarnings('ignore')

# read and preprocess db
df1 = pd.read_csv("messages_group_db.csv", sep="\t")
df1.sort_values(by='label', ascending=True, inplace=True)
df1.reset_index(inplace=True, drop=True)
df1 = df1.iloc[len(df1['label'])-df1[df1['label']==1].count().values[0]*2:,:]

# define X and y
X = df1['message']
tfidf = TfidfVectorizer(max_features=10000, ngram_range=(1,2))
X = tfidf.fit_transform(X)
y = df1['label']

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)

# LinearSVC
# train the model
# clf = LinearSVC()
# clf.fit(X_train, y_train)

# # accuracy score
# y_pred = clf.predict(X_test)
# from sklearn.metrics import accuracy_score
# print(f"Accuracy score of the model - {accuracy_score(y_test, y_pred)}")

# clf = LinearSVC()
# clf.fit(X, y)

# DecisionTreeClassifier
# clf = DecisionTreeClassifier(criterion='entropy', splitter='random', max_depth=None, max_features=None)
# clf.fit(X_train, y_train)

# # accuracy score
# y_pred = clf.predict(X_test)

# print(f"Accuracy score of the model - {accuracy_score(y_test, y_pred)}")

# clf = DecisionTreeClassifier(criterion='entropy', splitter='random', max_depth=None, max_features=None)
# clf.fit(X, y)

# RandomForestClassifier
clf = RandomForestClassifier(n_estimators = 150, criterion = 'entropy', max_depth=5, max_features='sqrt')
clf.fit(X_train, y_train)

# accuracy score
y_pred = clf.predict(X_test)

print(f"Accuracy score of the model - {accuracy_score(y_test, y_pred)}")

clf = RandomForestClassifier(n_estimators = 150, criterion = 'entropy', max_depth=5, max_features='sqrt')
clf.fit(X, y)


# load the trained model
pickle.dump(clf, open(f"{os.getcwd()}//DS_Model//trained_model.clf", "wb"))
