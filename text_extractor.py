import requests
from bs4 import BeautifulSoup

def scrape_webpage():
    url = "https://en.wikipedia.org/wiki/Ranni_the_Witch"
    response = requests.get(url)                  # no custom headers
    response.raise_for_status()                   # will throw on HTTP errors

    soup = BeautifulSoup(response.text, 'html.parser')
    content_div = soup.find('div', class_='mw-parser-output')
    paragraphs = content_div.find_all('p')        # assume it’s always there

    article_text = "\n\n".join(
        p.get_text(separator=" ", strip=True)
        for p in paragraphs
    )
    with open("Selected_Document.txt", "w", encoding="utf-8") as f:
        f.write(article_text)

    print(f"Success: extracted {len(paragraphs)} paragraphs.")
    return article_text

if __name__ == '__main__':
    scrape_webpage()
