# importing requests package
import requests


def NewsFromBBC():

    url="https://newsapi.org/v2/everything?q=bitcoin&apiKey=d9dd65752a814f88a95e84f142c67134"

    bbc = requests.get(url).json()

    article = bbc["articles"]
    source= []
    title= []
    author=[]
    url_click=[]
    description=[]


    for ar in article:
        source.append(ar["source"]["name"])
        author.append(ar["author"])
        title.append(ar["title"])
        url_click.append(ar["url"])
        description.append(ar["description"])
    f = open("news.txt", "w")
    for i in range(len(author) ):
        f.write("SOURCE : " + source[i] + "\n")
        f.write("AUTHOR : "+author[i] + "\n")
        f.write("TITLE : "+title[i] + "\n")
        f.write("URL : "+url_click[i] + "\n")
        f.write("DESCRIPTION : "+description[i] + "\n")
        f.write("**--**--**--**--**--**--**--**--**"+"\n")

    f.close()
if __name__ == '__main__':

    NewsFromBBC()
