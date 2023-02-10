import praw
from datetime import datetime
import json

def get_redditComments(cred, url, show_comments, select_comments, type_sort='top'):

    """
    reddit = praw.Reddit(
        client_id="---------",
        client_secret="-----------",
        password="",
        user_agent="-/------",
        username="",
    )
    """

    reddit = cred
    submission = reddit.submission(url=url)
    submission.comment_sort = type_sort
    comments = submission.comments
    title = submission.title

    print(submission.selftext)

    json_list = list()
    select_list = list()

    #Create selected list
    print()
    

    for i in range(show_comments):
        print(f"[{i}] - {comments[i].body}")
        print()


    print(" ----------END OF LIST -----------")
    print(f"Now, select all the {select_comments} comments\n")



    for i in range(select_comments):
        ind_select = int(input(f"Insert your {i} choice: "))
        select_list.append(ind_select)




    #write the comments(in the selected list)

    for i in select_list:

        autor = comments[i].author

        timestamp = comments[i].created_utc
        date_time = datetime.fromtimestamp(timestamp)
        date_time = date_time.strftime('%m/%d/%Y')


        d_post = date_time
        d_now = datetime.now().strftime('%m/%d/%Y')

        d_post = datetime.strptime(d_post, "%m/%d/%Y")
        d_now = datetime.strptime(d_now, "%m/%d/%Y")

        delta_days = d_now - d_post

        json_dict = {
            "titulo" : title,
            "autor": autor.name,
            "comentario": comments[i].body,
            "data" : f"· {delta_days.days} days ago",
            "respostas" : [{
                "autor_resp": "",
                "comentario_resp": "",
                "data_resp": ""
            },
            {
                "autor_resp": "",
                "comentario_resp": "",
                "data_resp": ""
            }
            ]
        }

        json_list.append(json_dict)


    # insert json title object first
    jsonTitle_dict = {
        "titulo" : title,
        "autor": autor.name,
        "selftext": submission.selftext,
        "data" : f"· {delta_days.days} days ago"
    }


    json_list.append(jsonTitle_dict)

    json_object = json.dumps(json_list)

    with open("comments_script.json", "w+") as outfile:
        outfile.write(json_object)



url = "https://www.reddit.com/r/RelatosDoReddit/comments/10bx70n/me_sinto_t%C3%A3o_sozinho/"


cred = praw.Reddit(
    client_id="PYFGWTGyI46_WGX3R3jYOw",
    client_secret="kmPvW3nrQQH0DTuUDqsGpsoDwUmi4g",
    password="",
    user_agent="u/theuserr",
    username="",
)

get_redditComments(cred, url, 5, 2, type_sort='top')




#este código captura apenas os principais comentários do post pelo id, sem ramificações. Ordena por "Melhor"