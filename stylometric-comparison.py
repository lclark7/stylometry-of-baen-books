!pip install plotly

import pandas as pd 
import numpy as np 
import plotly.graph_objects as go 
import plotly.express as px 
import glob
import os
from textblob import TextBlob
import nltk
nltk.download('punkt')
import plotly.io as pio

!unzip "/content/BaenBooksCorpus2.zip"

files = glob.glob("/content/BaenBooksCorpus2/*/*.txt")
print(files)

# Set up the dictionary 
dd ={
     "Author":[],
     "Path":[]
}

# a list of supposedly the most common 100 words
fwords = ["the","at","there","some","my","of","be","use","her","than","and","this","an","would","first","a","have","each","make","water","to","from","which","like","been","in","or","she","him","call","is","one","do","into","who","you","had","how","time","oil","that","by","their","has","its","it","word","if","look","now","he","but","will","two","find","was","not","up","more","long","for","what","other","write","down","on","all","about","go","day","are","were","out","see","did","as","we","many","number","get","with","when","then","no","come","his","your","them","way","made","they","can","these","could","may","I","said","so","people","part"]

# make an empty list for each word as a placeholder
for fw in fwords:
  dd[fw] = []

# just in case
files = glob.glob("/content/BaenBooksCorpus2/*/*.txt")


for file in files:
  # print current file to keep an eye on progress
  print(file)

  # get the author and filename from the path and add to dd
  dd['Author'].append(os.path.dirname(file).split("/")[-1])
  dd['Path'].append(os.path.basename(file))

  # read in the book's text
  with open(file,errors="surrogateescape") as f:
    text = f.read()

  # blobify and convert all words to lowercase
  blob = TextBlob(text)
  word_list = []
  for w in blob.words:
    word_list.append(w.lower())
  
  # get the frequency (per 10,000) for each frequent word
  for word in fwords:
    fr = (word_list.count(word) / len(word_list)) * 10000
    dd[word].append(fr)

df = pd.DataFrame(dd)

df

df = pd.DataFrame(dd)
fig = px.scatter(df, x="there", y="their", color="Author",hover_name="Path",symbol="Author")
fig.update_traces(marker=dict(size=20,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
fig.show()
