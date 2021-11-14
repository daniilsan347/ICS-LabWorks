# Laba No6 -- Web-scapping

import requests 
from bs4 import BeautifulSoup

news_feed = requests.get("https://espreso.tv/news")
news_feed_page = BeautifulSoup(news_feed.text, "html5lib")

html_news_list = news_feed_page.find("ul", id="js-news-list-container").find_all("li", class_="news_page_similar_content__item")

news_links = [li.find_all("a")[2]["href"] for li in html_news_list]

for nl in news_links:
    page_req = requests.get(nl)
    if page_req.ok:
        page_parse = BeautifulSoup(page_req.text, "html5lib")
        print("\n" + nl)
        print(page_parse.find("h1", class_="text-title").text, "\n")
        print("Кількість зображень у статті :" , len(page_parse.find("div", class_="news-content").find_all("img")))
        print("Кількість посилань  у статті :" , len(page_parse.find("div", class_="news-content").find_all("a")))
        print("")
        print("Як часто зустрічається слово \"США\" :", page_parse.find("div", class_="news-content").text.lower().split(" ").count("сша")/len(page_parse.find("div", class_="news-content").text.lower().split(" ")))
    else:
        print(nl, "404\n")