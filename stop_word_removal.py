import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
text="This is a practical class on NLP subject"
tokens=word_tokenize(text)
print(tokens)
stop_words=stopwords.words('english')
filtered_token=[]
for w in tokens:
    if w.lower() not in stop_words:
        filtered_token.append(w)
print(filtered_token)