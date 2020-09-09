# Sentiment Analysis Techniques
Detection of sentiment is an important part that helps in determining customer views. Multiple places use sentiment analysis are used like food review, movie review
and many more places. Thus, it forms very important part of any company. 

Here, few techniques for detecting sentiment are explained

### 1. Rule-based Apporach: 
This type of Sentiment analysis is performed by assigning sentiment to each word.
and than cummulative score is added for each of the word to infer whether it is positive or negative. VADER and TextBlob uses rule-based approach.

Advantages:
1. This approach is better for dataset of small size.
2. It does not required training time and can be implemented using library.

Disadvantages:
1. It is not good for determining mixed sense sentences. E.g. Irony, Sarcasm.
2. Although, already trained on multiple words, any out of vocabulary word is ignored. E.g. Typo's, social media trends.
3. It can not be trained to understand the word based on the context. E.g. he was happy vs he is happy provide the same result.
4. Change in word order provide the same result, so meaning of sentence is hard to obtain. E.g. playing not sleeping vs sleeping not playing.

### 2. Machine Learning: 
Instead of taking word as an individual, here complete sentence is taken into account and thus each word within can be trained differently. Multiple algorithm can
be used and tuning is easier. With good amount of training data it outperform Rule-based Approach.

Advantages:
1. It is able to detect sentence with mixed sense (E.g. not bad, too good).
2. Out of vocabulary can be taken into account while detecting sentiment.

Disadvantage:
1. Good quality labelled training data is required with big size.
2. Preprocessing take larger time than model creation.
3. The sequence of words are not taken into account and thus suffer from extracting meaning out of the sentence. 

### 3. Deep Learning:
This approach has outperformed both the above approach. Here, individual word, word sequence and symmentcs are considered. The evolution of RNN, LSTM and 
Bidirectional models have provided not only provided significant result but also form good pre-trained model like BERT, GPT, GPT-2 etc.
