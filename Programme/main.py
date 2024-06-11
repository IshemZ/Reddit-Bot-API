import praw # Reddit API
from variable import username, password, client_id, client_secret # Importing the variables from the variable.py file

reddit_instance = praw.Reddit(
    client_id = client_id,
    client_secret = client_secret,
    username = username,
    password = password,
    user_agent = "slack-bot"
)
#print(reddit_instance.user.me())
#subreddit = reddit_instance.subreddit("learnpython")
#print(subreddit)
#top_25_submissions = subreddit.hot(limit=25)
#for submissions in top_25_submissions:
#    print(submissions.title)
#subreddit = reddit_instance.subreddit("testingground4bots")
#subreddit.submit(title="This is a test", selftext="ceci est mon corps de texte ?" )

submissions = reddit_instance.submission('n1j2zg')
comments = submissions.comments
subreddit = submissions.subreddit

for comment in comments:
    if "uploads" in comment.body:
        print(subreddit.title)