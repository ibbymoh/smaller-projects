from bs4 import BeautifulSoup
import requests


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page,"html.parser",)
movie_list_scraped = soup.find_all(name="h3",class_="title")
movie_list = []

for movie in movie_list_scraped:
    movie_list.append(movie.getText())

movie_list.reverse()

for movie in movie_list:
    with open('movies_to_watch.txt','a', encoding="utf8") as m:
            m.write(movie + "\n")


