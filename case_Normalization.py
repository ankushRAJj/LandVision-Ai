import nltk
from nltk.tokenize import word_tokenize
document=['The cat sat on the mat','The dog chased the cat','The dog and cat are friends']
document_sent=[]
for doc in document:
    document_sent.append(doc.lower())
print(document_sent)