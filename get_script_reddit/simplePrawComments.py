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

    json_object = json.dumps(json_list)

    with open("comments_script.json", "w") as outfile:
        outfile.write(json_object)

"""
get_redditComments(cred, url, 2)


import enchant

# Create a dictionary for Brazilian Portuguese
dictionary = enchant.Dict("pt_BR")

# Check the spelling of a word
word = "se teletrankportar para onde você já está"
if dictionary.check(word):
    print(f"{word} is spelled correctly")
else:
    print(f"{word} is misspelled")
    print(f"Suggested corrections: {dictionary.suggest(word)}")
"""


#este código captura apenas os principais comentários do post pelo id, sem ramificações. Ordena por "Melhor"