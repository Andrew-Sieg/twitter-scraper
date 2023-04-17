# Script Author: Martin Beck
# Medium Article Follow-Along: https://medium.com/better-programming/how-to-scrape-tweets-with-snscrape-90124ed006af

# Pip install the command below if you don't have the development version of snscrape 
# !pip install git+https://github.com/JustAnotherArchivist/snscrape.git

# Run the below command if you don't already have Pandas
# !pip install pandas

# Imports
import os
import snscrape.modules.twitter as sntwitter
import pandas as pd
import openpyxl

# Below are two ways of scraping using the Python Wrapper.
# Comment or uncomment as you need. If you currently run the script as is it will scrape both queries
# then output two different csv files.

# Query by username
# Setting variables to be used below
maxTweets = 1000

# Creating list to append tweet data to
tweet_text = []

# Using TwitterSearchScraper to scrape data 
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('cousin willie popcorn since:2022-05-27 until:2023-04-09').get_items()):
    if i>maxTweets:
        break
    tweet_text.append([tweet.content,tweet.user.username])

# for i,tweet in enumerate(sntwitter.TwitterSearchScraper('launch darkly problems since:2022-05-27 until:2022-06-27').get_items()):
#     if i>maxTweets:
#         break
#     tweet_text.append([tweet.content,tweet.user.username])

####################################################################################################################################

# Creating a dataframe from the tweets list above
tweets_df1 = pd.DataFrame(tweet_text, columns=['tweet_text','Username'])

# Display first 5 entries from dataframe
# tweets_df1.head()

# Export dataframe into an Excel file
tweets_df1.to_excel('cousin-willie.xlsx', index = False, header=True)

os.system("start EXCEL.EXE cousin-willie.xlsx")