# importing libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Flatten, GlobalAveragePooling1D, Dense

# loading dataset
dataset = pd.read_csv('hotel_reviews.csv', delimiter='\t')
labels = dataset.Labels
reviews = dataset.Reviews

# text preprocessing
num_words = 2000
tokenizer = Tokenizer(num_words)
tokenizer.fit_on_texts(reviews)

# dicctionary with word-index pair
word_index = tokenizer.word_index

sentences = tokenizer.texts_to_sequences(reviews)
sequences = pad_sequences(sentences, padding='post', maxlen=20)
labels = np.array(labels)

# splitting into training and test dataset
x_train, x_test, y_train, y_test = train_test_split(sequences,labels,
                                                    test_size=0.2)

# hpyerparameters
vocab_size = num_words
embedding_dim = 16
max_len = 20
num_epochs = 25

# creating model
model1 = Sequential([
    Embedding(vocab_size, embedding_dim, input_length=max_len),
    GlobalAveragePooling1D(),
    Dense(6, activation='relu'),
    Dense(1, activation='sigmoid')
    ])

model1.summary()

# compiling model
model1.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

# training model
model1.fit(x_train, y_train, epochs=num_epochs, 
          validation_data=(x_test, y_test))


model2 = Sequential([
    Embedding(vocab_size, embedding_dim, input_length=max_len),
    Flatten(),
    Dense(6, activation='relu'),
    Dense(1, activation='sigmoid')
    ])

model2.summary()

# compiling model
model2.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

# training model
model2.fit(x_train, y_train, epochs=num_epochs, 
          validation_data=(x_test, y_test))

'''
Clearly results with GlobalAveragePooling1D is much more reliable than Flatten
'''
