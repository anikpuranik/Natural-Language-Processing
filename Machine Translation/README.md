## Machine Translation

Machine Translation is the technique of translating text from a source language into targeted language. There are in general three approaches for the MT:

#### 1. Rule-based:
For a rule based translation, knowledge of both source and target language is required. This requires extensive lexicons, syntactic and semantic information and 
is a large set of rules. This requires large dictionary and lingusitic rules. This approach is very time consuming and require lot of expense.

#### 2. Statistical:
This approach is based on the analysis of bilingual text corpora. With Bayes theorem, we can transform the occurance of word in one language to other.
SMT require three steps:

1. Language Model: What is the correct word given the context.
2. Translation Model: What is the best translation of a given word.
3. A method to find the right order of words.

#### 3. Neural Machine Translation:
This uses Seq2Seq models using neural network where instead of multiple networks only single network can be used. An encoder-decoder model is created using LSTM. Bidirectonal network or with attention model. This requires a large balanced bilingual dataset ro avoide the problem of out of vocabulary words.

### Implementation
Here, two scripts are present for the machine translation using Neural Network technique. 
1. LSTM Netowrk: This script uses the LSTM and Bidirectional LSTM model for conversion of German to English and the model is evaluated using actual results.
2. Pre-trained Modle: Here, we have implemented Google NMT that is an inbuilt as a part of TextBlob library. googletrans can also be used for the machine translation. An API is created using Streamlit and the demo is shown here (https://www.youtube.com/watch?v=C0Cvt2SihWQ)
3. LSTM Pre-trained: This is just a comparison script for the evaluation between Script1 and Script2.
