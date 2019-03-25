#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import all the libraries
import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt


# In[ ]:


#Get your Twitter API credentials and enter them here

consumer_key = "AC9hyVbyVb97m0j7KB6g98oN0"
consumer_s_key = "0uLpITgXF6twb6pw9s56nH9aO3ynkO70ijxfG6FF3qCM7shhox"

token_key = "1050058509176303617-xrVMbLZ48Wsdlq3hhzegBTgljWG0IQ" 
token_a_key = "2pCzOZuruWrWRCNJyxjC5sBmfAiQqD55S3pJFQ2mLb2QT"

# get authintic from your twitter api
auth = tweepy.OAuthHandler(consumer_key,consumer_s_key)
auth.set_access_token(token_key,token_a_key)
api = tweepy.API(auth)

# create empety list for store polarity of tweets
j = []
no_of_tweets = int(input("enter the no. of tweets you want to search"))
#get tweets
#if you only want the popular tweets sentiment analysis then change result_type "recent" to "popular"
tweets = tweepy.Cursor(api.search,q = "#mainbhichowkidaar",lang ="en",result_type = "recent").items(no_of_tweets)

#sentiment analysis on tweets
for i in tweets:
    print(i.text)
    
    #Remove "#" to know user_name, user's_location,tweet_source, date and time
    #print (i.user.name , i.user.location , i.source,i.created_at)
    
    analysis = TextBlob(i.text)
    polarity = analysis.sentiment.polarity
    print(polarity)
    j.append(polarity)
print(sum(j))
#finding average polarity of tweets 
avg = sum(j) /(no_of_tweets)
print("average polarity of tweets" + str(avg))

#for ploting line graph  
plt.plot(j)
plt.show()




# In[ ]:





# In[ ]:




