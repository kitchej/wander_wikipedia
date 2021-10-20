import re
import random
import sys

import requests
from bs4 import BeautifulSoup

DEFAULT_START = 'https://en.Wikipedia.org/wiki/Python_(programming_language)'
DEFAULT_ITERATIONS = 25
WIKI_URL_BASE = 'https://en.Wikipedia.org'
REGEX_PATTERN = re.compile(r'/wiki/\w+')


def follow_links_wikipedia(link, num_links_to_click, iterations=0):
    if iterations == num_links_to_click:
        print("")
        return link
    html = requests.get(link)
    if html.status_code == 404:
        print(f"Link: {link} cannot be reached")
        return link
    soup = BeautifulSoup(html.text, 'html.parser')
    a_tags = soup.find_all('a')
    page_links = [tag.get('href') for tag in a_tags if tag.get('href') is not None and
                  re.fullmatch(REGEX_PATTERN, tag.get('href')) is not None]
    if len(page_links) == 0:
        return link
    new_link = f"{WIKI_URL_BASE}{random.choice(page_links)}"
    print(f"Visiting: {new_link}")
    return follow_links_wikipedia(new_link, num_links_to_click, iterations + 1)


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'help':
            print("\n"
                  "WANDER.PY - Kill some time by wandering around Wikipedia\n"
                  "\n"
                  "Sometimes when I'm bored, I'll randomly click links on Wikipedia and see where I end up.\n"
                  "I decided to increase the fun by having a program do this for me, allowing me to click more links\n"
                  "and go further than I could on my own.\n"
                  "WARNING: It gets pretty slow when you get into the hundreds of links clicked!\n"
                  "\n"
                  "USAGE:\n"
                  "wander.py [Wikipedia article link] [number of links to click]\n"
                  "wander.py help\n"
                  "wander.py (defaults to Wikipedia page for python and clicks 25 links)\n")
            return
        else:
            start = sys.argv[1]
            try:
                iterations = sys.argv[2]
            except IndexError:
                print(f"Not enough arguments\n")
                print("USAGE:\n"
                      "wander.py [Wikipedia article link] [number of links to click]\n"
                      "wander.py help\n"
                      "wander.py (defaults to Wikipedia page for Python and clicks 25 links)\n")
                return

            if WIKI_URL_BASE not in start:
                print(f"Bad argument {start} for starting link. Must be a valid Wikipedia article link\n")
                print("USAGE:\n"
                      "wander.py [Wikipedia article link] [number of links to click]\n"
                      "wander.py help\n"
                      "wander.py (defaults to Wikipedia page for python and clicks 25 links)\n")
                return

            try:
                iterations = int(iterations)
                if iterations <= 0:
                    print(f"Bad argument {iterations} for number of links to click. "
                          f"Must be an positive, non-zero integer\n")
                    print("USAGE:\n"
                          "wander.py [Wikipedia article link] [number of links to click]\n"
                          "wander.py help\n"
                          "wander.py (defaults to Wikipedia page for python and clicks 25 links)\n")
                    return
            except ValueError:
                print(f"Bad argument {iterations} for iterations. Must be an positive integer\n")
                print("USAGE:\n"
                      "wander.py [Wikipedia article link] [number of links to click]\n"
                      "wander.py help\n"
                      "wander.py (defaults to Wikipedia page for python and clicks 25 links)\n")
                return

    else:
        start = DEFAULT_START
        iterations = DEFAULT_ITERATIONS

    print(f"Starting at: {start}")
    print("")
    print(f"You ended up at: {follow_links_wikipedia(DEFAULT_START, iterations)}")


if __name__ == '__main__':
    main()