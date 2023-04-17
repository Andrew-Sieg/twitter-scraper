import pandas as pd
from main import scrape_tweets

def test_scrape_tweets():
    # Call the function with sample arguments
    query = "OpenAI"
    start_date = "2022-01-01"
    end_date = "2022-01-02"
    max_tweets = 10
    tweets_df = scrape_tweets(query, start_date, end_date, max_tweets)

    # Check that the returned value is a pandas DataFrame
    assert isinstance(tweets_df, pd.DataFrame)

    # Check that the DataFrame has the expected columns
    expected_columns = ['tweet_text', 'Username']
    assert list(tweets_df.columns) == expected_columns

    # Check that the DataFrame has the expected number of rows
    expected_rows = max_tweets + 1 # account for header row
    assert len(tweets_df) == expected_rows

    # Check that the CSV file was created and has the expected name
    expected_filename = f'{query}.csv'
    import os
    assert os.path.isfile(expected_filename)

    # Remove the CSV file after the test completes
    os.remove(expected_filename)
