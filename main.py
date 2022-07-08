from operator import index
import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text

soup = BeautifulSoup(content,"html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movie_list = []

for movie in all_movies:
    title = movie.getText()
    movie_list.append(title)

movie_list.reverse()

with open('movies.txt', 'w') as f:
    for m in movie_list:
        f.write(m + '\n')
        
df = pd.read_fwf('movies.txt')
df.to_csv('movies.csv',index=False)