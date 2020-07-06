import requests

def newsfromapple():

    url="https://newsapi.org/v2/everything?q=apple&from=2020-06-27&to=2020-06-27&sortBy=popularity&apiKey=728858f0ea5e4b8eb9906c14fa71c8c7"

    apple = requests.get(url).json()
    article = apple["articles"]

    f = open("NewsArticle.txt", "w")
    for a in article:
        f.write("TITLE : " + a["title"] + "\n")
        f.write("DESCRIPTION : " + a["description"] + "\n")
        f.write("URL : "+ a["url"] + "\n")
        f.write("SOURCE : " + a["source"]["name"] + "\n")
        f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n\n")

    f.close()
if __name__ == '__main__':

    newsfromapple()
