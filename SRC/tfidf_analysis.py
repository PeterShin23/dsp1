#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 20:52:28 2023

@author: lucywang
"""

import pandas as pd
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.datasets import fetch_20newsgroups


data = pd.read_csv('consumer.csv') 
data = data.sample(frac = 1, random_state=42)
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


knn = KNeighborsClassifier(n_neighbors=7)

# training our classifier ; train_data.target will be having numbers assigned for each category in train data
clf = knn.fit(X_train_tfidf, train.rating)

# Input Data to predict their classes of the given categories
docs_new = ['This is a great product. I would recommend this to my friends.', 
            'I would use this tablet at work everyday.', 
            "This product doesn't work as well as I expected.",
            'I like this purchase and I would go back to buy more.', 
            'I recently bought a new tablet and I have to say, I absolutely love it! It is great for work and is so easy to use.',
            'I seldom use this tablet since is it so slow.',
            'This product was ok', 
            'This was an okay product',
            'Do not buy this.',
            'return',
            'This product is great. I would buy this product again', 
            'I hate this tablet and Amazon refused to offer me a refund.',
            'I love how easy to use this tablet is', 
            'Amazon charged me an extra fee. It took me a week to get my money back.',
            'I am very satisfied with my purchase and would definitely consider buying more of these tablets again.', 
            'I am really impressed with the quality of this product for the price.',
            'Overall, I would recommend this tablet to others.', 
            'I thought that this purchase would be a really good investment, but it broke the second day of using it.', 
            "I returned this product as it came in damaged. I won't be purchasing tablets from Amazon ever again."
            ]

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

