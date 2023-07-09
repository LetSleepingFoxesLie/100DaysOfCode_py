from bs4 import BeautifulSoup

html_content: str

with open(r"45_WebScraping\bs\website.html", "r", encoding = "utf8") as f:
    html_content = f.read()
    
soup = BeautifulSoup(html_content, "html.parser")
#print(soup.title)
#print(soup.title.string)

# Finding all <li> tags!
unordered_list_elements = soup.find_all(name = "li")
for li in unordered_list_elements:
    print(li.get_text())
    
# Getting references in anchor <a> tags
anchor_tags = soup.find_all(name = "a")
for anchor in anchor_tags:
    print(f"{anchor.get_text()} -> {anchor.get('href')}")
    
# Finding things with particular IDs
h1_example = soup.find(name = "h1", id = "name")
print(h1_example)

# And now finding with a specific class
# It uses an underscore to differentiate it from the usual "class" keyword!
section_heading = soup.find(name = "h3", class_ = "heading")
print(section_heading)
print(section_heading.get("class"))
print(section_heading.get_text())
print(section_heading.name)

# Using CSS selectors
# We're going to get the only anchor that sits within a paragraph tag
company_url = soup.select_one(selector = "p a")
print(company_url)

# And now we're going to select by ID
company_name = soup.select_one(selector = "#name")
print(company_name)

# And now by class!
headings = soup.select(".heading")
print(headings)