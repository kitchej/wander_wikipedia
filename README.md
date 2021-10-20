# WANDER.PY - Kill Some Time by Wandering Around Wikipedia

Sometimes when I'm bored, I'll randomly click links on Wikipedia and see where I end up. I decided to write a program do this for me, 
allowing me to sit back and relax while a computer does the hard work of clicking links.

## Some Fun Results: 
>You started at: Python (Programming Language) | Link: https://en.wikipedia.org/wiki/Python_(programming_language)  
>You wandered to: Antisemitism | Link: https://en.wikipedia.org/wiki/Antisemitism

>You started at: Mickey Mouse | Link: https://en.wikipedia.org/wiki/Mickey_Mouse  
>You wandered to: Soviet Union | Link: https://en.wikipedia.org/wiki/Soviet_Union     

>You started at: Taylor Swift | Link: https://en.wikipedia.org/wiki/Taylor_Swift  
>You wandered to: Crucifixion Of Jesus | Link: https://en.wikipedia.org/wiki/Crucifixion_of_Jesus

## Requirements
* Beautiful Soup 4
* Requests

## Commands

*** You may need to put your link in quotes if using Powershell ***  

`wander.py [Wikipedia article link] [number of links to click]`  

`wander.py [Wikipedia article link] [number of links to click] [seed]`  

`wander.py help`  

`wander.py` Starts at the Wikipedia page for Python and clicks 25 links

## Other Languages

If you want to wander Wikipedia in a language other than English, simply change the ```WIKI_URL_BASE``` variable to the base Wikpedia URL of your target language. 

Examples:  
```python
WIKI_URL_BASE = "https://es.wikipedia.org" # Spanish 
```
```python
WIKI_URL_BASE = "https://de.wikipedia.org" # German  
```
```python
WIKI_URL_BASE = "https://zh.wikipedia.org" # Chinese
``` 

## Seeds
Optionally, you can pass a third argument specifying the seed you want to use. The program will also output the seed it used. This feature is useful for debugging, but if the _any_ of the articles in the chain are edited, you won't get the same results even when using the same seed.