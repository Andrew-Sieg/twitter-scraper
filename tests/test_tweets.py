# test_scraping.py

import pytest
import os
import pandas as pd
from twitter_scraper.main import scrape_tweets


@pytest.fixture
def sample_tweets_df():
    return pd.DataFrame([['test tweet 1', 'user1'], ['test tweet 2', 'user2']], columns=['tweet_text', 'Username'])

def test_scrape_tweets(sample_tweets_df, mocker):
    # Mocking the TwitterSearchScraper object
    scraper_mock = mocker.Mock()
    scraper_mock.get_items.return_value = [mocker.Mock(rawContent='test tweet 1', user=mocker.Mock(username='user1')),
                                           mocker.Mock(rawContent='test tweet 2', user=mocker.Mock(username='user2'))]
    mocker.patch('snscrape.modules.twitter.TwitterSearchScraper', return_value=scraper_mock)
    
    # Calling the function
    scrape_tweets('twin spires', '2023-04-10', '2023-04-17')
    
    # Checking if the dataframe created by the function is equal to the expected dataframe
    assert sample_tweets_df.equals(pd.read_excel('twin-spires.xlsx', index=False))
    
    # Cleaning up the created Excel file
    os.remove('twin-spires.xlsx')
