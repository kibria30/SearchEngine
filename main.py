import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_website(startUrl, maxPages=10):
    pagesToVisit = [startUrl]
    visitedPages = set()
    pagesContent= []

    while pagesToVisit and len(visitedPages) < maxPages:
        url = pagesToVisit.pop(0)    # pop from first as queue
        if url in visitedPages:
            continue

        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            links = soup.find_all("a")
            for link in links:
                pagesToVisit.append(link.get("href"))
                print(link.get("href"))

        except Exception as e:
            print(f"Error crawling {url}: {e}")

        visitedPages.add(url)


crawl_website("https://example.com", maxPages=3)