from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()
    

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

all_anchor_tags = soup.find_all(name="p")
# print(all_anchor_tags)
for tag in all_anchor_tags:
    tag.get("")
    # print(tag.getText())

# isolate a specific h1 with id
heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())
print(section_heading.name)
