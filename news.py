from bs4 import BeautifulSoup
import bs4 as bs
import requests
import urllib.request

f = open("content.txt", "w")

# init source
ori_url = 'https://www.vox.com/'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

# Make request to the URL
html = requests.get(ori_url, headers=headers)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(html.text, "html.parser")
#print(soup)

# get the content from the index page
print("Main News")
# find all the <div> with class:"c-newspaper__column"
for paragraph in soup.find_all("div", attrs = {"class" : "c-newspaper__column"}):
  # find all the <a> with "data-analytics-link" : "article"
  for title in paragraph.find_all("a", attrs = {"data-analytics-link" : "article"}):
    print("Title: ",str(title.text))
    # write the title into content.txt
    f.write("Title: ")
    f.write(str(title.text))
    f.write("\n")
    # get the url of the news, then switch it as a new source
    print("url: ", title.get('href'))
    url = title.get('href')
    html = requests.get(url, headers=headers)
    new_soup = BeautifulSoup(html.text, "html.parser")
    for external in new_soup.find_all("div", attrs = {"class" : "c-entry-content"}):
      print("Content: ")
      for text in external("p"):
        # write the content into content.txt
        print(str(text.text).strip())
        f.write(str(text.text).strip())
      f.write("\n")

  for title in paragraph.find_all("a", attrs = {"data-analytics-link" : "feature"}):
    print("Title: ",str(title.text))
    f.write("Title: ")
    f.write(str(title.text))
    f.write("\n")
    print("url: ", title.get('href'))
    url = title.get('href')
    html = requests.get(url, headers=headers)
    new_soup = BeautifulSoup(html.text, "html.parser")
    for external in new_soup.find_all("div", attrs = {"class" : "c-entry-content"}):
      print("Content: ")
      for text in external("p"):
        print(str(text.text).strip())
        f.write(str(text.text).strip())
      f.write("\n")
      
print("Column News")
for paragraph in soup.find_all("div", attrs = {"class" : "l-col__main"}):
  for title in paragraph.find_all("a", attrs = {"data-analytics-link" : "article"}):
    print("Title: ",str(title.text))
    f.write("Title: ")
    f.write(str(title.text))
    f.write("\n")
    print("url: ", title.get('href'))
    url = title.get('href')
    html = requests.get(url, headers=headers)
    new_soup = BeautifulSoup(html.text, "html.parser")
    for external in new_soup.find_all("div", attrs = {"class" : "c-entry-content"}):
      print("Content: ")
      for text in external("p"):
        print(str(text.text).strip())
        f.write(str(text.text).strip())
      f.write("\n")

for paragraph in soup.find_all("div", attrs = {"class" : "l-col__main"}):
  for title in paragraph.find_all("a", attrs = {"data-analytics-link" : "feature"}):
    print("Title: ",str(title.text))
    f.write("Title: ")
    f.write(str(title.text))
    f.write("\n")
    print("url: ", title.get('href'))
    url = title.get('href')
    html = requests.get(url, headers=headers)
    new_soup = BeautifulSoup(html.text, "html.parser")
    for external in new_soup.find_all("div", attrs = {"class" : "c-entry-content"}):
      print("Content: ")
      for text in external("p"):
        print(str(text.text).strip())
        f.write(str(text.text).strip())
      f.write("\n")
f.close()

# if you want to read directly from the text file
'''
f = open("content.txt", "r")
print(f.read())
f.close()
'''
