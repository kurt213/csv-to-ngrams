import pandas as pd
import re
import os, sys

import nltk
from nltk.util import ngrams
from nltk import FreqDist

# Set path depending on running .exe or .py
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    application_path = os.path.dirname(sys.executable)
    os.chdir(application_path)

# Download for tokenize functionality
nltk.download('punkt')

# Import csv
df = pd.read_csv('input.csv', header=None)

print('CSV read successfully')

# Get Series
tweet_list = df[0]

# Clean tweets - removes any HTML and punctuation
clean_tweets = []

print('Cleaning text')

for t in tweet_list:
    t = re.sub(r'(<br />)|(<br>)|(\\n)|(\\r)|-', " ", str(t))
    t = re.sub(r'[\.,()+…?!"/:@\'“]', "", str(t))
    t = re.sub(r'(&amp;)', "and", str(t))
    t = " ".join(t.split())
    clean_tweets.append(t)
    
print('Creating n-grams...')

# Join into one string and change to lower case
# Tokenize 
all_tweets = " ".join(clean_tweets).lower()
token_tweets = nltk.word_tokenize(all_tweets)

# Create n-grams
tweet_sgrams = ngrams(token_tweets, 1)
tweet_bigrams = ngrams(token_tweets, 2)
tweet_trigrams = ngrams(token_tweets, 3)
tweet_quadgrams = ngrams(token_tweets, 4)
tweet_pentgrams = ngrams(token_tweets, 5)

# Create Frequency Distributions
tweet_fds = FreqDist(tweet_sgrams)
tweet_fdb = FreqDist(tweet_bigrams)
tweet_fdt = FreqDist(tweet_trigrams)
tweet_fdq = FreqDist(tweet_quadgrams)
tweet_fdp = FreqDist(tweet_pentgrams)

# Convert to DataFrames
df_tweet_sgram = pd.DataFrame.from_dict(tweet_fds, orient='index', columns=['freq']).reset_index().sort_values(by=['freq'], ascending=False)
df_tweet_bigram = pd.DataFrame.from_dict(tweet_fdb, orient='index', columns=['freq']).reset_index().sort_values(by=['freq'], ascending=False)
df_tweet_trigram = pd.DataFrame.from_dict(tweet_fdt, orient='index', columns=['freq']).reset_index().sort_values(by=['freq'], ascending=False)
df_tweet_quadgram = pd.DataFrame.from_dict(tweet_fdq, orient='index', columns=['freq']).reset_index().sort_values(by=['freq'], ascending=False)
df_tweet_pentgram = pd.DataFrame.from_dict(tweet_fdp, orient='index', columns=['freq']).reset_index().sort_values(by=['freq'], ascending=False)

print("n-grams created successfully.")
print("saving excel... this may take a few moments")

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('ngrams_output.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df_tweet_sgram.to_excel(writer, sheet_name='single-ngram')
df_tweet_bigram.to_excel(writer, sheet_name='bigram')
df_tweet_trigram.to_excel(writer, sheet_name='trigram')
df_tweet_quadgram.to_excel(writer, sheet_name='quadgram')
df_tweet_pentgram.to_excel(writer, sheet_name='pentgram')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

print('Excel file written successfully')