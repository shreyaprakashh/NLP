#SENTIMENT ANALYSIS
from textblob import TextBlob
feedback1 = "The food at the restaurant was awesome"
feedback2 = "The food at the restaurant was very good"
blob1 = TextBlob(feedback1)
blob2 = TextBlob(feedback2)
print(blob1.sentiment)
print(blob2.sentiment)
