from bs4 import BeautifulSoup
import requests

url = "https://appbrewery.github.io/news.ycombinator.com/"
response = requests.get(url)
yc_web_page = response.text


soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)


article_upvotes = [int(score.getText().split(" ")[0])
                   for score in soup.find_all(name="span", class_='score')]

max_score = max(article_upvotes)
max_score_index = article_upvotes.index(max_score)
max_score_text = article_texts[max_score_index]
max_score_link = article_links[max_score_index]

print(max_score_text)
print(max_score_link)
print(max_score)
