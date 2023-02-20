#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 20:52:28 2023

@author: lucywang
@author: petershin
"""

import pandas as pd
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.datasets import fetch_20newsgroups


data = pd.read_csv('Desktop/1429_1.csv') 
data = data.sample(frac = 1)
data = data.rename(columns={"reviews.text": "text", "reviews.rating": "rating"})
data = data[data['text'].notna() & data['rating'].notna()]
train = data.head(int(len(data)*(70/100)))
test = data.tail(int(len(data)*(30/100)))
    
count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(train.text)
X_train_counts
# transform a count matrix to a normalized tf-idf representation (tf-idf transformer)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)


knn = KNeighborsClassifier(n_neighbors=3)

# training our classifier ; train_data.target will be having numbers assigned for each category in train data
clf = knn.fit(X_train_tfidf, train.rating)

# Input Data to predict their classes of the given categories
docs_new = ['This is a great product', 'This is an ok product']
# building up feature vector of our input
X_new_counts = count_vect.transform(docs_new)
# We call transform instead of fit_transform because it's already been fit
X_new_tfidf = tfidf_transformer.transform(X_new_counts)


predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
    print('%r => %d' % (doc, category))
    
    
    
# We can use Pipeline to add vectorizer -> transformer -> classifier all in a one compound classifier
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', knn),
])
# Fitting our train data to the pipeline
text_clf.fit(train.text, train.rating)


docs_test = test.text
# Predicting our test data
predicted = text_clf.predict(docs_test)
print('We got an accuracy of',np.mean(predicted == test.rating)*100, '% over the test data.')

