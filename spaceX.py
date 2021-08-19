import urllib.request
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
response=urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')

html=response.read()
soup=BeautifulSoup(html,'html5lib')
text=soup.get_text(strip=True)
#print(text)


#convert the text into tokens
tokens=[t for t in text.split()]
#print(tokens)
sr=stopwords.words('english')
clean_token=tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_token.remove(token)

freq=nltk.FreqDist(clean_token)
for key,value in freq.items():
    print(str(key)+":"+str(value))

freq.plot(20, cumulative=False)



