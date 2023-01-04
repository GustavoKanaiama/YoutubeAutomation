import praw

reddit = praw.Reddit(
    client_id="PYFGWTGyI46_WGX3R3jYOw",
    client_secret="kmPvW3nrQQH0DTuUDqsGpsoDwUmi4g",
    password="",
    user_agent="u/theuserr",
    username="",
)

submission = reddit.submission(id='1027p2f')

comments = submission.comments

for comment in comments:
    print(comment.body)


#este código captura apenas os principais comentários do post pelo id, sem ramificações. Ordena por "Melhor"