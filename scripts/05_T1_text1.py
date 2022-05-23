#
# Data transformation step by step
#

# conda install -c anaconda nltk
import nltk
nltk.download('punkt')
import nltk.corpus


text = 'This I is the! first document waiting.  Baby and babies .  Likes and like.  Walk and walked'

#Lower case
text = "".join(x.lower() for x in text.split('. '))

# Removing Punctuation
import string
import re
text = re.sub('['+string.punctuation+']', '', text)

# Word tokenize
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)

# stop words
from nltk.corpus import stopwords
nltk.download('stopwords')
stop = stopwords.words('english')
tokens = [x for x in tokens if x not in stop]

# Stemmer
from nltk.stem import PorterStemmer
pst = PorterStemmer()
tokens = [pst.stem(x) for x in tokens]

#  Lemmatizer
#from nltk.stem import WordNetLemmatizer
#nltk.download('wordnet')
#lemmatizer = WordNetLemmatizer() 
#tokens = [lemmatizer.lemmatize(x) for x in tokens]

# Counting
from nltk.probability import FreqDist
counting = FreqDist(tokens)



