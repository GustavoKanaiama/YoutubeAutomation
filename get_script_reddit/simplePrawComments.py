import praw
from datetime import datetime
import json
from googletrans import Translator

def translate(texto):

    translator = Translator(service_urls=[
    'translate.google.com'])

    return translator.translate(texto, dest='pt', src='en').text

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

        author_obj = autor

        if author_obj == None:
            author_name = '*deleted'
        else: author_name = autor.name

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
            "autor": author_name,
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

    with open("comments_script.json", "w+") as outfile:
        #outfile.write("aaaaaaaaaaa")
        outfile.write(json_object)

def get_redditComments_en(cred, url, show_comments, select_comments, type_sort='top'):

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
    title = translate(submission.title)

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

        author_obj = autor

        if author_obj == None:
            author_name = '*deleted'
        else: author_name = autor.name

        

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
            "autor": author_name,
            "comentario": translate(comments[i].body),
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

    with open("comments_script.json", "w+") as outfile:
        #outfile.write("aaaaaaaaaaa")
        outfile.write(json_object)


"""
cred = praw.Reddit(
    client_id="PYFGWTGyI46_WGX3R3jYOw",
    client_secret="kmPvW3nrQQH0DTuUDqsGpsoDwUmi4g",
    password="",
    user_agent="u/theuserr",
    username="",
)

number_show_comments = 20
number_selected_comments = 3

url = 'https://www.reddit.com/r/AskReddit/comments/ak76pa/what_are_things_you_can_say_during_sex_and_a/'

get_redditComments_en(cred, url, number_show_comments, number_selected_comments, type_sort='top')

"""

#este código captura apenas os principais comentários do post pelo id, sem ramificações. Ordena por "Melhor"