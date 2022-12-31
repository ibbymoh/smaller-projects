from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,"html.parser")
entries = soup.find_all(name="span",class_="titleline")
scores = soup.find_all(name="span",class_="score")
num_entries = len(scores)
article_title = []
article_links = []
article_votes = []


for i in range(num_entries):
    title = entries[i].select("a")[0].getText()
    article_title.append(title)

    link = entries[i].select("a")[0]["href"]
    article_links.append(link)

    score =int(scores[i].getText().split()[0])
    article_votes.append(score)

max_vote_index = article_votes.index(max(article_votes))



print(article_votes[max_vote_index])
print(article_links[max_vote_index])
print(article_title[max_vote_index])


























# with open('website.html' , encoding="utf8") as f:
#
#
#     contents = f.read()
#
# #helps beautiful soup understand what we are parsing
# soup = BeautifulSoup(contents,'html.parser')
#
# #potential things we can do
#
# # #1. make things neater
# # print(soup.prettify())
# #
# # #2. get title
# #
# # print(soup.title)
# #
# # #3. get title string
# #
# # print(soup.title.string)
#
# all_anchor_tags = soup.find_all(name="a")
#
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# get_heading = soup.find(name="h3",class_="heading")
# print(get_heading.getText())