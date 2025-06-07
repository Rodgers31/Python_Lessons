from bs4 import BeautifulSoup
import requests

respose = requests.get("https://news.ycombinator.com/")
ycdata = respose.text

soup = BeautifulSoup(ycdata, 'html.parser')

article_texts = []
article_links = []
article_scores = []

# Get all span tags containing articles
spans = soup.find_all("span", {"class": "titleline"})
# Get all span tangs containing scores
spans_score = soup.find_all("span", {"class": "score"})

# Get all article texts and url from spans containing articles
article_texts = [a.find('a').getText() for a in spans]
article_links = [a.find('a').get("href") for a in spans]
# Get all scores from spans containing scores
article_scores = [int(score.getText().split()[0]) for score in spans_score]

print(article_texts)
print(article_links)
print(article_scores)

# Get index of highest score
index = article_scores.index(max(article_scores))

# Print story title, link and votes of story with highest votes.
print(
    f"Story with highest upvotes.\nTitle: {article_texts[index]}\nUrl: {article_links[index]}\nVotes: {article_scores[index]}")


