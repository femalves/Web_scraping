# https://www.rithmschool.com/blog

import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])
    for article in articles:
        a_tag = article.find("a")
        # title
        title = a_tag.get_text()
        # href
        url = a_tag['href']
        # date
        date = article.find("time")["datetime"]
        csv_writer.writerrow([title, url, date])