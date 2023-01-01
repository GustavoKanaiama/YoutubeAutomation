import praw

reddit = praw.Reddit(
    client_id="PYFGWTGyI46_WGX3R3jYOw",
    client_secret="kmPvW3nrQQH0DTuUDqsGpsoDwUmi4g",
    password="",
    user_agent="u/theuserr",
    username="",
)

subreddit = reddit.subreddit("test")

#for submission in reddit.subreddit("desabafos").hot(limit=25):
 #   print(submission.title)

for submission in reddit.subreddit("desabafos+PergunteReddit").top(limit=25):
    print(submission.title)