import re
import random
import sys

import requests
from bs4 import BeautifulSoup

DEFAULT_START = 'https://en.Wikipedia.org/wiki/Python_(programming_language)'
WIKI_URL_BASE = 'https://en.wikipedia.org'  # Change this url if you want wikipedia in a different language
WIKI_ARTICLE_PATTERN = re.compile(r'/wiki/\w+')
URL_PATTERN = re.compile(r'https?://.+\.org.+')


class UrlChain:
    def __init__(self):
        self._chain = []

    def __str__(self):
        return str(self._chain)

    def __iter__(self):
        return self._chain

    def __len__(self):
        return len(self._chain)

    def __getitem__(self, i):
        return self._chain[i]

    def __setitem__(self, i, item):
        self._chain[i] = item

    def append(self, value):
        self._chain.append(value)

    def split(self, token):
        token_indexes = []
        out = []
        start = 0
        for i, url in enumerate(self._chain):
            if url == token:
                token_indexes.append(i)
        for i in token_indexes:
            out.append(self._chain[start:i])
            start = i + 1

        return out


URL_CHAIN = UrlChain()


def show_usage():
    print("find_hitler.py <link>")


def get_article_name(link):
    return link.split("/")[-1].replace("_", " ").title()


def follow_links_recursive(link, iterations=0, branches=0):
    global URL_CHAIN
    if iterations == 100:
        return
    html = requests.get(link)
    print(f"Visiting {link}")
    if html.status_code == 404:
        return
    URL_CHAIN.append(link)
    soup = BeautifulSoup(html.text, 'html.parser')
    a_tags = soup.find_all('a')
    page_links = [tag.get('href') for tag in a_tags if tag.get('href') is not None and
                  re.fullmatch(WIKI_ARTICLE_PATTERN, tag.get('href')) is not None and
                  tag.get('href') != "/wiki/Main_Page"]
    if len(page_links) == 0:
        return
    if "/wiki/Adolf_Hitler" in page_links:
        URL_CHAIN.append(f"{WIKI_URL_BASE}/wiki/Adolf_Hitler")
        return
    elif "/wiki/Germany" in page_links:
        new_link = f"{WIKI_URL_BASE}/wiki/Germany"
        follow_links_recursive(new_link, iterations + 1)
    elif "/wiki/Europe" in page_links:
        new_link = f"{WIKI_URL_BASE}/wiki/Europe"
        follow_links_recursive(new_link, iterations + 1)
    elif "/wiki/World_War_I" in page_links:
        new_link = f"{WIKI_URL_BASE}/wiki/World_War_I"
        follow_links_recursive(new_link, iterations + 1)
    elif "/wiki/World_War_II" in page_links:
        new_link = f"{WIKI_URL_BASE}/wiki/World_War_II"
        follow_links_recursive(new_link, iterations + 1)
    elif "/wiki/War" in page_links:
        new_link = f"{WIKI_URL_BASE}/wiki/War"
        follow_links_recursive(new_link, iterations + 1)
    else:
        follow_links_recursive(f"{WIKI_URL_BASE}{random.choice(page_links)}", iterations + 1)


def main():
    args = sys.argv
    if len(args) < 2:
        show_usage()

    link = args[1]
    if not re.fullmatch(URL_PATTERN, link):
        print(f"Bad argument {link} for starting link. Must be a valid Wikipedia Article Link\n"
              f"Example: https://en.Wikipedia.org/wiki/Python_(programming_language)\n")
        show_usage()
        return

    if WIKI_URL_BASE not in link:
        print(f"Bad argument {link} for starting link. Must be a valid Wikipedia article link\n"
              f"Example: https://en.Wikipedia.org/wiki/Python_(programming_language)\n")
        show_usage()
        return

    if link == f"{WIKI_URL_BASE}/wiki/Adolf_Hitler":
        print("Found 1 path to Hitler smartass")

    follow_links_recursive(link)
    if len(URL_CHAIN) != 0:
        print("")
        shortest_path = URL_CHAIN[0]
        possible_paths = URL_CHAIN.split(f"{WIKI_URL_BASE}/wiki/Adolf_Hitler")
        for path in possible_paths:
            if len(path) < len(shortest_path):
                shortest_path = path

        print(f"Found a path to Adolf Hitler:")
        for url in shortest_path:
            print(url)
            print("\t\t|\n\t\tV")
        print(f"{WIKI_URL_BASE}/wiki/Adolf_Hitler")
    else:
        print("Could not find a path to Adolf Hitler")


if __name__ == '__main__':
    main()
