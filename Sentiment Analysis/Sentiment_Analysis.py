# importing libraries
import re
import pandas as pd
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import naive_bayes, linear_model, svm
from sklearn.metrics import confusion_matrix

# loading dataset
dataset = pd.read_csv('Sentiments.csv', delimiter='\t')
labels = dataset.Labels
reviews = dataset.Reviews

# text preprocessing
for ind,text in tqdm(enumerate(reviews)):
    text = re.sub('[.]','',text.lower()).split()
    review = [word 
              for word in text
              if (word.isalpha()
              and len(word)>1)
              ]
    reviews[ind] = ' '.join(review)

# creating vectors
vectorizer1 = TfidfVectorizer()
reviews1 = vectorizer1.fit_transform(reviews)
reviews1 = reviews1.toarray()

vectorizer2 = CountVectorizer()
reviews2 = vectorizer2.fit_transform(reviews)
reviews2 = reviews2.toarray()

# vocabulary of words
vocab = list(set(vectorizer1.get_feature_names()))

# splitting into train and test
x_train_tfidf, x_test_tfidf, y_train_tfidf, y_test_tfidf = train_test_split(reviews1, labels, test_size=0.2)
x_train_cv, x_test_cv, y_train_cv, y_test_cv = train_test_split(reviews2, labels, test_size=0.2)

model = [naive_bayes.GaussianNB ,linear_model.LogisticRegression, svm.SVC]

# training and compiling the model
def model_designing(model, x, y):
    # training the model
    model = model()
    model.fit(x, y)
    return model

models_tfidf = [model_designing(model[i], x_train_tfidf, y_train_tfidf) for i in range(3)]
models_cv = [model_designing(model[i], x_train_cv, y_train_cv) for i in range(3)]

def prediction_evulation(model, x_test1):
    # testing model
    y_pred1, y_pred2, y_pred3 = [model[i].predict(x_test1) for i in range(3)]
    return y_pred1, y_pred2, y_pred3

y_tfidf = prediction_evulation(models_tfidf, x_test_tfidf)
y_cv = prediction_evulation(models_cv, x_test_cv)

# confusion_martix
def confusion_martices(y, y_pred, dataset_name, model_name) :
        y_pred = confusion_matrix(y, y_pred)
        print("Result for "+dataset_name+" and "+model_name+":\n", 
              y_pred,"\n",
              "Correct prediction are:",sum(y_pred.diagonal()),"\n")
        
for j,algorithm in  enumerate(["logistic regression","naive bayes","svm"]):
    confusion_martices(y_tfidf[j], y_test_tfidf, 'tf-idf', algorithm)
    confusion_martices(y_cv[j], y_test_cv, 'cv', algorithm)
        

'''Result for tf-idf and logistic regression:
 [[59 17]
 [45 79]] 
 Correct prediction are: 138
 
Result for cv and logistic regression:
 [[56 12]
 [47 85]] 
 Correct prediction are: 141
 
Result for tf-idf and naive bayes:
 [[86 16]
 [18 80]] 
 Correct prediction are: 166
 
Result for cv and naive bayes:
 [[84 17]
 [19 80]] 
 Correct prediction are: 164
 
Result for tf-idf and svm:
 [[88 19]
 [16 77]] 
 Correct prediction are: 165
 
Result for cv and svm:
 [[85 24]
 [18 73]] 
 Correct prediction are: 158
 '''
