# WANDER.PY - Kill some time by wandering around Wikipedia

Sometimes when I'm bored, I'll randomly click links on Wikipedia and see where I end up. I decided to write a program do this for me, 
allowing me to sit back and relax while a computer does the hard work of clicking links.

If you want to wander Wikipedia in a language other than English, simply change the WIKI_URL_BASE variable to the base Wikpedia URL of your target language.    
Examples:  
WIKI_URL_BASE = "https://es.Wikipedia.org" # Spanish  
WIKI_URL_BASE = "https://de.Wikipedia.org" # German    
WIKI_URL_BASE = "https://zh.Wikipedia.org" # Chinese


USAGE:  
*** You may need to put your link in quotes if using Powershell ***  
wander.py [Wikipedia article link] [number of links to click]  
wander.py help  
wander.py (defaults to the english Wikipedia page for python and clicks 25 links)
