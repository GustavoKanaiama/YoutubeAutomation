import requests
from bs4 import BeautifulSoup
import json

def get_criptonews_json(number_selected_news):

    # Faz a requisição à página da web
    url = 'https://cointelegraph.com.br/'
    page = requests.get(url)

    # Cria o objeto BeautifulSoup a partir do conteúdo da página
    soup = BeautifulSoup(page.content, 'html.parser')

    selected_news = list()

    # Visualize news
    news_soupObj = soup.find_all("article", {"class": "post-card__article"})

    cont = 0
    print()
    for i in news_soupObj:
        print("[" + str(cont) +"]" + i.find_all("a")[1].text) #print the news title
        print()
        cont += 1

    print("---------- ENDING OF GETTING NEWS ----------")
    print(f"Select your {number_selected_news} news.\n")

    #select news
    for i in range(number_selected_news):
        var = int(input(f"Digite a noticia [{i}]: "))
        selected_news.append(var)



    # Getting selected news data to json
    list_json = list()

    for i in range(number_selected_news):

        obj_var = news_soupObj[i].find_all("a")

        news_type = obj_var[0].text #tipo de noticia
        news_title = obj_var[1].text #titulo
        author = obj_var[2].text #autor
        news_lead = news_soupObj[i].find("p").text #lead do texto
        news_datetime = news_soupObj[i].time["datetime"] #datetime

        json_dict = {
            "news_type": news_type,
            "news_title": news_title,
            "author": author,
            "news_lead": news_lead,
            "news_datetime": news_datetime,
            "title_and_lead": news_title + ". " + news_lead # for create reading voice
        }

        list_json.append(json_dict)

    print("--------- JSON CREATED SUCCESSFULL -------\n")
    json_object = json.dumps(list_json)

    with open("json_files/cripto_news.json", "w+") as outfile:
        outfile.write(json_object)

get_criptonews_json(2)