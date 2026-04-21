import nltk
from nltk.stem import PorterStemmer
ps=PorterStemmer()
from nltk.tokenize import word_tokenize
text="organize organized organizing organizes"
tokens=word_tokenize(text)
stemmed_token=[]
for w in tokens:
    t=ps.stem(w)
    stemmed_token.append(t)

print(stemmed_token)