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


# Query by username
# Setting variables to be used below
maxTweets = 1000

# Creating list to append tweet data to
tweet_text = []

# Using TwitterSearchScraper to scrape data 
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('twin spires since:2023-04-10 until:2023-04-17').get_items()):
    if i>maxTweets:
        break
    tweet_text.append([tweet.rawContent, tweet.user.username])

####################################################################################################################################

# Creating a dataframe from the tweets list above
tweets_df1 = pd.DataFrame(tweet_text, columns=['tweet_text','Username'])

# Display first 5 entries from dataframe
# tweets_df1.head()

# Export dataframe into an Excel file
tweets_df1.to_excel('twin-spires.xlsx', index = False, header=True)

os.system("start EXCEL.EXE twin-spires.xlsx")