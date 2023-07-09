import requests as rq
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
OUTPUT_FILE_PATH = r"45_WebScraping\100-movies\movies.txt"

# Write your code below this line 👇

# 1. Make request and create soup object
response = rq.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Get the list of articles: an h3 with a class "title"?
entries = soup.find_all(name = "h3", class_ = "title")

# Now use list comprehension to reverse the list...
# We could have just used entries.reverse() somewhere, but I don't give a fuck, right?
entries = [e.text + "\n" for e in entries[::-1]]

# Now let's write everything to the file:

try:
    with open(file = OUTPUT_FILE_PATH, mode = "w", encoding = "utf-8") as f:
        f.writelines(entries)
        print("Done!")
except FileNotFoundError:
    print("Shrug")