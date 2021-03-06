from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html, "lxml")

# dumb one
# for link in bsObj.findAll("a"):
#     if "href" in link.attrs:
#         print(link.attrs['href'])

# print([link.attrs['href'] for link in bsObj.findAll("a") if "href" in link.attrs])

#improved version with only article pages
# for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",
# href=re.compile("^(/wiki)((?!:).)*$")):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])


#Better version

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "lxml")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")


    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print("-------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")
