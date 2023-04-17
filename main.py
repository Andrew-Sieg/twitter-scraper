import snscrape.modules.twitter as sntwitter
import pandas as pd


def scrape_tweets(query: str = None, start_date: str = None, end_date: str = None, max_tweets: int = None) -> pd.DataFrame:
    if query is None:
        query = input("Enter the Twitter search query you want to scrape: ")
    if start_date is None:
        start_date = input("Enter the start date (YYYY-MM-DD) for scraping tweets: ")
    if end_date is None:
        end_date = input("Enter the end date (YYYY-MM-DD) for scraping tweets: ")
    if max_tweets is None:
        max_tweets = int(input("Enter the maximum number of tweets you want to scrape: "))

    tweet_text = []

    # Using TwitterSearchScraper to scrape data
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{query} since:{start_date} until:{end_date}').get_items()):
        if i > max_tweets:
            break
        tweet_text.append([tweet.rawContent, tweet.user.username])

    # Creating a dataframe from the tweets list above
    tweets_df = pd.DataFrame(tweet_text, columns=['tweet_text', 'Username'])

    # Write results to a csv file which is named after the query
    tweets_df.to_csv(f'{query}.csv', index=False)
    print(f'Results saved to {query}.csv')

    

    return tweets_df
         

if __name__ == '__main__':
    scrape_tweets()
