# Custom News API Library

Utilizes BeautifulSoup to scrape common search engine news

Requirements:
* Python 3.x
* BeautifulSoup


No endpoints, user keys are currently supported. Just copy **fetchNews.py** 
and **TagCleaner.py** into your project and import as any other module:

```python

from fetchNews import formatUrl, scraper

myLocation = "Roswell, NM"
fullUrl = formatUrl(myLocation)
results = scraper(fullUrl)

#print the first headline from the newsfeed
print(results['hlines'][0])

```

Future Updates:

* Selectable variety of search engines to gather news
* Support user keys, JSON return formats