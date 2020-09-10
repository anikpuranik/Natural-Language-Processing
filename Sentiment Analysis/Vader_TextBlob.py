# importing libraries
import numpy as np
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# loading dataset
dataset = pd.read_csv('Sentiments.csv', delimiter='\t')
#labels = dataset.Labels
#reviews = dataset.Reviews

# initializing Sentiment analysis class
vader_score = np.array([None]*len(dataset))
sent_analysis = SentimentIntensityAnalyzer()

for ind,review in enumerate(dataset.Reviews):
    scores = sent_analysis.polarity_scores(review)
    vader_score[ind] = scores['compound']
    
vader_predictions = np.array(vader_score > 0.5, dtype=int)
print(sum(vader_predictions==dataset.Labels))

'''
Result for VADER :  775
'''
