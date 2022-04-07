import praw



reddit=praw.Reddit(

            client_id='sO1ypuzMA0DRwgD8aLcHCQ',
            client_secret='AAfpbdUosIlYfaxSjWuYzPDJ8rzqQA',
            username='',
            password='',
            user_agent='RedditCommentSearch'

            )

SubRedditToSearch=reddit.subreddit(input("Input your favorite subreddit"))
print(SubRedditToSearch)

for submission in reddit.subreddit(str(SubRedditToSearch)).top(limit=5):
    print(submission.title)
    print(submission.url)


#for submission in reddit.subreddit("Starcraft").top("all"):
#    print(submission.title)

