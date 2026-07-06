# Web Scrapping Practice
import threading
import requests
from bs4 import BeautifulSoup
urls = [
'https://docs.langchain.com/oss/python/learn',
'https://docs.langchain.com/oss/python/langchain/overview',
'https://docs.langchain.com/oss/python/langgraph/overview',]

def fetch_content(urs):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f"Total number of characters: {len(soup.text)} are in this url{url},")

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All Web pages fetched")