# -*- coding: utf-8 -*-
"""NLP_Group_93_Food_Review.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jacen8wvzEJhNyXa3kASsRB0pwrBY5YH

<h1><center><b>NLP Assignment 2

Set A
Group- 93

Members:

ARUN KUMAR K- 2022aa05152@wilp.bits-pilani.ac.in

SANDEEP JOSHI- 2022ac05241@wilp.bits-pilani.ac.in

SHERINE JOY- 2022ac05483@wilp.bits-pilani.ac.in

THOMAS.K.JOHN- 2022ac05620@wilp.bits-pilani.ac.in
</b></center></h1>
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import gensim
from gensim import corpora
from gensim.models import LdaModel
from gensim.utils import simple_preprocess
from multiprocessing import process
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud

nltk.download('punkt')
nltk.download('stopwords')

#Load the first 10000 rows in the dataset
df = pd.read_csv('/content/drive/MyDrive/Assignment_2/Reviews.csv', nrows=10000)

"""Question 1: Perform EDA and necessary pre-processing steps in dataset."""

# Understanding the structure of the dataset
print(df.head())

from itertools import chain

# Load the corpus of text documents
df = pd.read_csv('/content/drive/MyDrive/Assignment_2/Reviews.csv', nrows=10000)

# Preprocess text data
def preprocess_text(text):
    return [token for token in simple_preprocess(text) if token not in gensim.parsing.preprocessing.STOPWORDS]

processed_data= [preprocess_text(text) for text in list(df["Text"])]
flattened_list = list(chain.from_iterable(processed_data))

# Create dictionary and corpus
dictionary = corpora.Dictionary(processed_data)
corpus = [dictionary.doc2bow(text) for text in processed_data]

# Print vocabulary size
print("\nVocabulary size:", len(dictionary))

# Tokenization using NLTK
tokenized_docs = [word_tokenize(" ".join(doc).lower()) for doc in processed_data]

# Filter out stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [[word for word in doc if word not in stop_words] for doc in tokenized_docs]

# Count word frequency
word_freq = Counter([word for doc in filtered_tokens for word in doc])

# Print most common words
print("Most common words:")
print(word_freq.most_common())

# Visualize word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(word_freq))
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Most Common Words')
plt.show()

"""Question 2: Using the LDA algorithm create the Topics"""

# Build LDA model
lda_model = LdaModel(corpus=corpus,
                     id2word=dictionary,
                     num_topics=10,
                     random_state=42,
                     update_every=1,
                     chunksize=100,
                     passes=10,
                     alpha='auto',
                     per_word_topics=True)

"""Question 3: Compute the coherence score and print Topics Extracted"""

# Print top 10 words for each topic
for topic in lda_model.print_topics(num_topics=10, num_words=10):
    print(topic)

# Evaluate LDA model
coherence_model_lda = gensim.models.CoherenceModel(model=lda_model, texts=processed_data, dictionary=dictionary, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print(f"Coherence score: {coherence_lda}")

"""Question 4: Visualize the topics"""

topics = lda_model.show_topics(formatted=False)

# Visualize Topic-Word Distribution
for topic_idx, topic in topics:
    words = [word for word, _ in topic]
    weights = [weight for _, weight in topic]
    plt.figure(figsize=(8, 6))
    plt.barh(words, weights, color='skyblue')
    plt.gca().invert_yaxis()
    plt.title(f'Topic {topic_idx + 1}')
    plt.xlabel('Word Weight')
    plt.ylabel('Word')
    plt.show()

"""Question 5: *Plot* the dependency parser for any two random sentences from the entire corpus/dataset that has at least 10 words in the sentence. Make sure that dependency parser looks good and should visually understandable."""

import random
import spacy
from spacy import displacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Filter sentences with at least 10 words
filtered_sentences = [sent for sent in list(df["Text"]) if len(sent.split()) >= 10]

# Select two random sentences
random_sentences = random.sample(filtered_sentences, 2)

# Process each sentence with spaCy
parsed_sentences = [nlp(sentence) for sentence in random_sentences]

# Plot the dependency parsers
for i, parsed_sentence in enumerate(parsed_sentences):
    displacy.render(parsed_sentence, style="dep", jupyter=True, options={"distance": 120})