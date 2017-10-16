from fetchNews import formatUrl, scraper

myLocation = "Roswell, NM"
fullUrl = formatUrl(myLocation)
results = scraper(fullUrl)

#print the first headline from the newsfeed
print(results['hlines'][0])