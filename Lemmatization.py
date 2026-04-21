import nltk
from nltk.stem import WordNetLemmatizer
lem=WordNetLemmatizer()
text="organizes"
output=lem.lemmatize(text,pos='v')
print(output)