#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 20:52:01 2023

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
import matplotlib.pyplot as plt

data = pd.read_csv('Documents/consumer.csv')
data = data.sample(frac = 1)
data = data.rename(columns={"reviews.text": "text", "reviews.rating": "rating"})
data = data[data['text'].notna() & data['rating'].notna()]
train = data.head(int(len(data)*(70/100)))
test = data.tail(int(len(data)*(30/100)))

TrainData = train['text']
labels = train['rating']

TestData = test['text']

from sklearn.feature_extraction.text import CountVectorizer
bow_vectorizer = CountVectorizer(max_features=100, stop_words='english')

X_train = TrainData
y_train = labels
bowVect = bow_vectorizer.fit(X_train)


bowTrain = bowVect.transform(X_train)
bowTest = bowVect.transform(TestData)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 3)
bowTrain
knn.fit(bowTrain, y_train)
predict = knn.predict(bowTest[0:11000])


d = {'text': test['text'], 
    'actual': test['rating'],
    'predicted': predict}
df = pd.DataFrame(data=d)

#get accuracy by comparing actual vs prediction values
total_num = len(df)
num_predict_correct = len(df[df['actual'] == df['predicted']])
acc = num_predict_correct/total_num
acc







#do same thing but get rid of "neutral" words from EDA
data = pd.read_csv('Documents/consumer.csv')
data = data.sample(frac = 1)
data = data.rename(columns={"reviews.text": "text", "reviews.rating": "rating"})
data = data[data['text'].notna() & data['rating'].notna()]
data['text'] = data['text'].str.lower()
data["text"] = data['text'].str.replace('[^\w\s]','')
banned = ['tablet', 'tablets', 'amazon', 'one', 'kindle', 'kindles', 'would', 'fire', 'device', 'devices', 'time', 'product', 'products']
f = lambda x: ' '.join([item for item in x.split() if item not in banned])
data["text"] = data["text"].apply(f)


train = data.head(int(len(data)*(70/100)))
test = data.tail(int(len(data)*(30/100)))

TrainData = train['text']
labels = train['rating']

TestData = test['text']

from sklearn.feature_extraction.text import CountVectorizer
bow_vectorizer = CountVectorizer(max_features=100, stop_words='english')

X_train = TrainData
y_train = labels
bowVect = bow_vectorizer.fit(X_train)


bowTrain = bowVect.transform(X_train)
bowTest = bowVect.transform(TestData)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 3)
bowTrain
knn.fit(bowTrain, y_train)
predict = knn.predict(bowTest[0:11000])

d = {'text': test['text'], 
     'actual': test['rating'],
    'predicted': predict}
    
df = pd.DataFrame(data=d)

#get accuracy by comparing actual vs prediction values
total_num = len(df)
num_predict_correct = len(df[df['actual'] == df['predicted']])
acc = num_predict_correct/total_num
acc




#test different neighbors

#columns: actual, predicted, difference, row number
d2 = {'text': test['text'], 
     'actual': test['rating'],
     'predicted': predict,
     'difference': predict - test['rating']}
d2 = pd.DataFrame(data=d2)

d2 = d2.groupby('difference')
d2.head(10).sort_values('difference', ascending=False)

d2_sorted = d2['difference'].value_counts().sort_index()
d2_sorted = d2_sorted.to_frame()
ax = d2_sorted.plot.bar(y='difference', rot=0, legend=False)
plt.xlabel("Rating Difference (Predicted - Actual)")
plt.ylabel("Frequency")
plt.title("Distribution of Rating Differences (Predicted - Actual)")













