import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_website(startUrl, maxPages=10):
    pagesToVisit = list(startUrl)
    visitedPages = set()
    pagesContent= []

    while pagesToVisit and len(visitedPages) < maxPages:
        url = pagesToVisit.pop(0)    # pop from first as queue

        if url in visitedPages:
            continue

        if not url.startswith(("http://", "https://", "/")):
            print(f"Skipping non-HTTP URL: {url}")
            continue

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            title = soup.title.string.strip() if soup.title else "No Title"
            content = soup.get_text()

            pagesContent.append({
                "title" : title,
                "content" : content,
                "url" : url
            })

            for link in soup.find_all("a", href=True):
                href = link["href"].strip()
                if href.startswith("#"):
                    continue

                full_url = urljoin(url, href)
                if full_url not in visitedPages:
                    pagesToVisit.append(full_url)

            visitedPages.add(url)

        except Exception as e:
            print(f"Error crawling {url}: {e}")

    return pagesContent

# pagesContent = crawl_website(["https://www.geeksforgeeks.org/", "https://www.wikipedia.org/"], maxPages=100)

pagesContent = crawl_website(["https://www.geeksforgeeks.org/", "https://www.wikipedia.org/"], 10)
for i in pagesContent:
    print(i["url"])
