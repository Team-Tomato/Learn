import csv
import json
import requests

# Input:
# data.csv --> movies name as a single column without header
# year --> Manually a variable
#
# Output:
# result2.csv --> Extracted data
# moviesnotFount.csv --> Movies which dont have data in omdb API

print("Enter the year of the movie collection : ", end="")
inputYear = int(input())
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        movie = row[0]
        movie.replace(" ","+")
        url = "http://www.omdbapi.com/?t=" + movie + "&y=" + str(inputYear) + "&apikey=1cf7cfa6"
        response = requests.get(url)
        responseData = json.loads(response.text)
        if len(responseData) == 0:
            print("null")
        else:
            if(responseData['Response'] == 'True'):
                title = responseData['Title']
                year = responseData['Year']          
                genre = responseData['Genre']
                director = responseData['Director']
                write = responseData['Writer']
                actor = responseData['Actors']
                language = responseData['Language']
                country = responseData['Country']
                awards = responseData['Awards']
                rating = responseData['imdbRating']
                with open('result2.csv', 'a', newline='') as foptr:
                    writer = csv.writer(foptr)
                    writer.writerow([title,year,"",genre,director,write,actor,language,country,awards,rating])        
            else:
                with open('moviesnotFount.csv', 'a', newline='') as foptr2:
                    writer2 = csv.writer(foptr2)
                    writer2.writerow([movie.replace("+"," ")])
