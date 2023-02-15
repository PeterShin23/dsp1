#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 03:58:40 2023

@author: lucywang
"""

import os, json, gzip 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plot

import string
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet, stopwords

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
 

#os.getcwd()

data = pd.read_csv('Documents/consumer.csv') 
df = data[["reviews.text", "reviews.rating"]]

# drop any rows w/ missing values
df = df.dropna()
# discover the actual counts
df = df.rename(columns={"reviews.text": "text", "reviews.rating": "rating"})
rating_counts = df.rating.value_counts() 
# set sample size to labels w/ minimum count
sample_size = 402
df_equal_rating = pd.DataFrame()
for i in df.rating.unique():
  X = df[df.rating == i].sample(sample_size)
  df_equal_rating = df_equal_rating.append(X)

stopwords_list = stopwords.words('english')

def ReviewProcessing(df):
  # remove non alphanumeric 
  df['review_cleaned'] = df.text.str.replace('[^a-zA-Z0-9 ]', '')
  # lowercase
  df.review_cleaned = df.review_cleaned.str.lower()
  # split into list
  df.review_cleaned = df.review_cleaned.str.split(' ')
  # remove stopwords
  df.review_cleaned = df.review_cleaned.apply(lambda x: [item for item in x if item not in stopwords_list])
  return df

def get_wordnet_pos(word):
  tag = nltk.pos_tag([word])[0][1][0].upper()
  tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

  return tag_dict.get(tag, wordnet.NOUN)

lemmatizer = nltk.stem.WordNetLemmatizer()
def get_lemmatize(sent):
  return " ".join([lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(sent)])


clean_data = ReviewProcessing(df_equal_rating)
clean_data.review_cleaned = clean_data.review_cleaned.apply(' '.join)
clean_data['review_cleaned_lemmatized'] = clean_data.review_cleaned.apply(get_lemmatize)
clean_data #contains column with rating 


def tokenize(string):
   return nltk.word_tokenize(string)

def count_words2(word):
    m[word] = m[word] + 1 if word in m else 1

def count_words(list_words):
    for word in list_words:
        count_words2(word)

review_text = clean_data['review_cleaned_lemmatized']

tokenized_reviews = review_text.apply(tokenize)
tokenized_reviews

m = {}

tokenized_reviews.apply(count_words)
sorted_words = sorted(m.items(), key=lambda x: x[1], reverse=True)

for word in sorted_words:
	print(word[0], word[1])

top_20 = sorted_words[:20]
top_20 = pd.DataFrame(top_20, columns=['word', 'count'])
top_20

ax = top_20.plot(x='word', y='count', kind='bar', legend=False, rot=0)
plt.tight_layout()
plt.xlabel("Word")
plt.ylabel("Count")
plt.title("Count of Top 20 Words Over All Reviews")
plt.xticks(rotation=60)



#rating 1
review_text_1 = clean_data[clean_data['rating'] == 1.0]
review_text_1 = review_text_1['review_cleaned_lemmatized']
review_text_1

tokenized_reviews_1 = review_text_1.apply(tokenize)
tokenized_reviews_1

m = {}

tokenized_reviews_1.apply(count_words)

sorted_words_1 = sorted(m.items(), key=lambda x: x[1], reverse=True)

top_10_1 = sorted_words_1[:10]
top_10_1 = pd.DataFrame(top_10_1, columns=['word', 'count'])
top_10_1

ax = top_10_1.plot(x='word', y='count', kind='bar', legend=False, rot=0)
plt.tight_layout()
plt.xlabel("Word")
plt.ylabel("Count")
plt.title("Count of Top 10 Words in Reviews with Rating 1")
plt.xticks(rotation=60)







#rating 5
review_text_5 = clean_data[clean_data['rating'] == 5.0]
review_text_5 = review_text_5['review_cleaned_lemmatized']
review_text_5

tokenized_reviews_5 = review_text_5.apply(tokenize)
tokenized_reviews_5

m = {}

tokenized_reviews_5.apply(count_words)

sorted_words_5 = sorted(m.items(), key=lambda x: x[1], reverse=True)

top_10_5 = sorted_words_5[:10]
top_10_5 = pd.DataFrame(top_10_5, columns=['word', 'count'])
top_10_5


ax = top_10_5.plot(x='word', y='count', kind='bar', legend=False, rot=0)
plt.tight_layout()
plt.xlabel("Word")
plt.ylabel("Count")
plt.title("Count of Top 10 Words in Reviews with Rating 5")
plt.xticks(rotation=60)








#Frequency of Ratings Over All Reviews
rating_counts = df.rating.value_counts().rename_axis('rating').reset_index(name='counts')
rating_counts = rating_counts.sort_values(by=['rating'])
rating_counts

ratings = list(rating_counts['rating'])
counts = list(rating_counts['counts'])

ax = rating_counts.plot(x='rating', y='counts', kind='bar', legend=False, rot=0)
plt.tight_layout()
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.title("Frequency of Ratings Over All Reviews")
   




    
