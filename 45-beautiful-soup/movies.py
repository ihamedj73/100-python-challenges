import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
res = requests.get(URL)
site_content = res.text

soup = BeautifulSoup(site_content, "html.parser")

movies_title_tag = soup.find_all(name="h3", class_="title")
movies_title = [title.getText() for title in movies_title_tag]
movies_title.reverse()


with open("movies.txt", mode="w", encoding="utf-8") as file:
    content = "\n".join(movies_title)
    file.write(content)
