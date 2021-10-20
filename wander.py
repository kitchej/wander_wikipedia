import re
import random
import sys

import requests
from bs4 import BeautifulSoup

DEFAULT_START = 'https://en.Wikipedia.org/wiki/Python_(programming_language)'
DEFAULT_ITERATIONS = 25
WIKI_URL_BASE = 'https://en.wikipedia.org'  # Change this url if you want wikipedia in a different language
REGEX_PATTERN = re.compile(r'/wiki/\w+')


def show_usage():
    print("USAGE:\n"
          "NOTE: You may need to put the link in quotes if using Powershell \n"
          "wander.py [Wikipedia article link] [number of links to click]\n"
          "wander.py [Wikipedia article link] [number of links to click] [seed]\n"
          "wander.py help\n"
          "wander.py (defaults to Wikipedia page for python and clicks 25 links)\n")


def get_article_name(link):
    return link.split("/")[-1].replace("_", " ").title()


def follow_links_wikipedia(link, num_links_to_click, iterations=0):
    """Recursive function that randomly follows links in a wikipedia page"""
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
                  re.fullmatch(REGEX_PATTERN, tag.get('href')) is not None and
                  tag.get('href') != "/wiki/Main_Page"]
    if len(page_links) == 0:
        return link
    new_link = f"{WIKI_URL_BASE}{random.choice(page_links)}"
    print(f"Visiting: {get_article_name(new_link)} | Link: {new_link}")
    return follow_links_wikipedia(new_link, num_links_to_click, iterations + 1)


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'help':
            print("\n"
                  "WANDER.PY - Kill some time by wandering around Wikipedia\n"
                  "\n"
                  "Sometimes when I'm bored, I'll randomly click links on Wikipedia and see where I end up.\n"
                  "I decided to write a program do this for me, allowing me to sit back and relax while a computer\n"
                  "does the hard work of clicking links.\n"
                  "\n")
            show_usage()
            return
        else:
            start = sys.argv[1]
            try:
                iterations = sys.argv[2]
            except IndexError:
                print(f"Not enough arguments\n")
                show_usage()
                return

            try:
                seed = sys.argv[3]
                seed = int(seed)
            except IndexError:
                seed = random.randint(0, sys.maxsize)
            except ValueError:
                print(f"Bad argument {sys.argv[3]} for seed. Seed must be an integer")
                show_usage()
                return

            if WIKI_URL_BASE not in start:
                print(f"Bad argument {start} for starting link. Must be a valid Wikipedia article link\n"
                      f"Example: https://en.Wikipedia.org/wiki/Python_(programming_language)\n")
                show_usage()
                return

            try:
                iterations = int(iterations)
            except ValueError:
                print(f"Bad argument {iterations} for iterations. Must be an positive, non-zero integer\n")
                show_usage()
                return

            if iterations <= 0:
                print(f"Bad argument {iterations} for number of links to click. "
                      f"Must be an positive, non-zero integer\n")
                show_usage()
                return
    else:
        start = DEFAULT_START
        iterations = DEFAULT_ITERATIONS
        seed = random.randint(0, sys.maxsize)

    random.seed(seed)
    print("")
    end = follow_links_wikipedia(start, iterations)
    print(f"You started at: {get_article_name(start)} | Link: {start}")
    print(f"You wandered to: {get_article_name(end)} | Link: {end}")
    print(f"Seed: {seed}")
    print("")


if __name__ == '__main__':
    main()
