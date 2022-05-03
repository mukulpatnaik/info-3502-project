import pandas as pd
from datetime import datetime

from psaw import PushshiftAPI
api = PushshiftAPI()

start_epoch = int(pd.to_datetime('2020-09-01').timestamp())
end_epoch = int(pd.to_datetime('2021-06-30').timestamp())

x = api.search_comments(after=start_epoch, before=end_epoch, # these are the unix-based timestamps to search between
                             subreddit=['wallstreetbets'], 
                             filter=['id','url','author', 'title', 'score','subreddit','selftext','num_comments'], # list of fields to return
                             num_comments=">100",
                             limit = 50000 # limit on the number of records returned
                              )

y = api.search_submissions(after=start_epoch, before=end_epoch, # these are the unix-based timestamps to search between
                             subreddit=['wallstreetbets'], 
                             filter=['id','url','author', 'title', 'score','subreddit','selftext','num_comments'], # list of fields to return
                             num_comments=">100",
                             limit = 50000 # limit on the number of records returned
                              )

p = list(x)
c = list(x)

posts = pd.DataFrame.from_dict(p)
comments = pd.DataFrame.from_dict(p)

posts.to_csv('wsb_posts.csv')
comments.to_csv('wsb_comments.csv')