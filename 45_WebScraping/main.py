from bs4 import BeautifulSoup
import requests as rq

from article import Article

response = rq.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

entries = soup.select(selector  = ".titleline a")

# Took me an hour to figure this one out. Thanks, ChatGPT!
entries = [e for e in entries if e.find(class_ = "sitestr") is None]
scores = soup.select(selector  = ".score")

article_list = []
index = 0

for entry in entries:
    article_list.append(Article(
        title = entry.text,
        link = entry.get("href"),
        score = int(scores[index].text.split(" ")[0])
        )
    )
    
    index += 1

# Sorting
article_list.sort(key = lambda x: x.score, reverse = True)

# Printing the sorted list
for a in article_list:
    print(f"{a.title} -> {a.score} points")