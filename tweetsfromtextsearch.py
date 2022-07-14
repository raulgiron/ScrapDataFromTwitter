import snscrape.modules.twitter as sntwitter
import pandas as pd
import numpy as np


desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 10)

# Creating list to append tweet data to
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper('sex for grades since:2021-07-05 until:2022-07-06').get_items()):
    if i > 150:
        break
    attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.rawContent])

# Creating a dataframe to load the list
tweets_df = pd.DataFrame(attributes_container,
                         columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])


print(tweets_df.head(10))
