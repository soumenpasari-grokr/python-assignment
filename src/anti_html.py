import requests
from bs4 import BeautifulSoup

def download_html_page(web_link):
    # getting text from request
    website_content = requests.get(web_link)
    # parsing the website content
    soup = BeautifulSoup(website_content.text,'html.parser')
    # getting all the text inside the website content 
    article_text = soup.find('body').text
    # returning the text inside the website
    return article_text

print(download_html_page('https://academichelp.net/samples/creative-writing-samples/article-samples/eternal-existence.html'))