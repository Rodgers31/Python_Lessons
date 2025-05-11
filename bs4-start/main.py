from bs4 import BeautifulSoup

with open(file="website.html") as f:
    contents = f.read()
    

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)


all_anchor_tags = soup.find_all(name="p")
print(all_anchor_tags)
for tag in all_anchor_tags:
    tag.get("")
    # print(tag.getText())

