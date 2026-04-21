import nltk
from nltk.tokenize import word_tokenize
text="we are studing INT344 now and doing practical"
s=word_tokenize(text)
print(s)

token=["the","cat","sat","on","the","mat","mat","sat"]
unique_token=list(set(token))
print(unique_token)