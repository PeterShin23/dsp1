# Amazon Reviews Sentiment Anaysis

## SRC

### Installing/Building Code
All source code for this project is located in the SRC folder in this repository....

### Code Usage

## DATA

### Data Dictionary
Attribute  | Description
------------- | -------------
Categories  | keywords regarding type of product
reviews.doRecommend  | Whether user recommends product
reviews.numHelpful  |  Number of users who find review helpful
reviews.rating  | Rating of review
reviews.text  | Content of Review
reviews.title  | Title/header of review

Link to data: https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products?fbclid=IwAR0yIq8hjHkHZTXoqGVG2xiIQunCDA0JI1ChlZ5XhSZulLyZReaQnheRv-4&select=1429_1.csv

### Revelant Notes
- The data set includes 34,000 consumer reviews of Amazon products such as TVs, computers, speakers, headphones, and more. This data set is a subset of a larger data set acquired from Datafiniti, which is a database that obtains product data from websites. Each individual row represents a single amazon review and the columns represent a different attribute regarding that specific review like date, helpfulness score, recommendation, reviewer username, etc. We retrieved this data on KAGGLE (linked above) in the form of a CSV and will be primarily focused on review text and review rating.
- The whole data set includes three files. We will only use the file named "1429_1.csv" throughout this project
- We removed all "reviews.text" empty/null entries

## FIGURES
***All figures located in "FIGURES" folder
File Name  | Title  | Summary
------------- | ------------- | -------------
![alt text](https://github.com/lucywang-uva/dsp1/blob/main/FIGURES/top20_all.png?raw=true) | Many of the top 20 words have an subjectively positive connotation, including “great”, “good”, “bought”, “like”, “love” and “well”. There seems to be little to no words with a subjectively negative connotation. While there are a majority of positive connotation words, we cannot conclude that these words necessarily are used in a context that yields or prompt a higher rating review
top10_rating1  | Count of Top 10 Words in Reviews with Rating 1 | Many of the top 10 words in reviews with a rating of 1 have mostly subjectively neutral descriptive words other than “return” which is subjectively negative
top10_rating5  | Count of Top 10 Words in Reviews with Rating 5 | Compared to the top 10 words of all reviews, reviews with a rating of 5 have more top 10 words that explicitly a positive connotation such as “love”, “great”, “east”, “get”, and “bought”
rating_distribution  | Frequency of Ratings Over All Reviews | The distribution of ratings across all reviews shows very few reviews with a rating of 1 to 3, with most reviews being a 5 star rating. This distribution correlates with our findings of the top 20 words in reviews as most descriptive words we observed are positive
rating_diff  | Frequency of Ratings Differences (Predicted - Actual) | The distribution of predicted - actual ratings found with test data. Distribution shows majority of predictions by model makes an accurate prediction of actual rating. However, our model still makes some very inaccurate predictions as shown by 4 and -4 rating differences.





## REFERENCES
[1]	“Consumer reviews of Amazon Products,” Kaggle, 20-May-2019. [Online]. Available: https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products?Fbclid=IwAR0yIq8hjHkHZTXoqGVG2xiIQunCDA0JI1ChlZ5XhSZulLyZReaQnheRv-4&select=1429_1.csv. [Accessed: 14-Feb-2023]. 

[2]	“Amazon ecommerce trends for 2023,” Insider Intelligence, 06-Jan-2023. [Online]. Available: https://www.insiderintelligence.com/insights/amazon-ecommerce-trends/. [Accessed: 08-Feb-2023]. 




