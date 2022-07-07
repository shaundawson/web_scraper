import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
page = response.text

soup = BeautifulSoup(page,"html.parser")
articles = soup.find_all(name="a", class_="titlelink")

article_texts = []
article_links = []

for article_tag in articles:
        article_text = article_tag.getText()
        article_texts.append(article_text)
        article_link = article_tag.get("href")
        article_links.append(article_link)
    
article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]



print(article_texts)
print(article_links)
print(int(article_upvotes[0].split()[0]))