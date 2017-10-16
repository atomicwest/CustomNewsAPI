from bs4 import BeautifulSoup as bsp
import bs4      #only used for class check
from urllib.request import urlopen, Request
from TagCleaner import tagCleaner
import re

#replace spaces in a query such as "roswell, nm"
def concatQ(string, sym):
    words = string.split(" ")
    return sym.join(words)

'''
==============================================
google news search pages have each of the stories encased in a 
    class called "g_cy" with several child classes for other elements:
        - top _xGs _SHs | r : news link in a href attr
        - th _RGs | th: thumbnail in src attr
        - l _PMs | r : headline AND news link 
        
        - _OHs _PHs | f : news source
        - f nsa _QHs | slp: date (or how many mins/hrs ago if same day)
        - st | st:  news summary

        tablecol1 tablecol2
        th          f
                    slp
                    st

==============================================
'''

#the full url should look like:
#https://www.google.com/search?tbm=nws&q=new+zealand

# genericUrl = "https://www.google.com/search?source=hp&q="
genericUrl = "https://www.google.com/search?tbm=nws&q="

query = "Portland, Maine"
formatQ = concatQ(query, "+")
fullurl = genericUrl + formatQ

mod = "-slp-class"

fname = "read-" + query + mod + ".txt"


def scraper(url):
    try:
        head = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url, headers=head)
        html = urlopen(req)
        bsObj = bsp(html, "html.parser")
        
        #scrape raw tags first
        imgs = bsObj.findAll('img', {'class':'th'})
        headlines = bsObj.findAll('h3', {'class':'r'})
        links = bsObj.findAll('span', {'class':'f'})
        dates = bsObj.findAll('div', {'class':'slp'})
        stories = bsObj.findAll('div', {'class':'st'})
        
        # print(len(imgs))
        # print(len(headlines))
        # print(len(links))
        # print(len(dates))
        # print(len(stories))
        
        
        
        #extract from scraped data
        #each data array may not be the same length; 
        #try to match domains to align arrays
        thumbs = [t['src'] for t in imgs]
        
        # if s is a hashed news headline link: s.split("=")[1].split("&")[0]
        hlinks = [h.a['href'].split("=")[1].split("&")[0] for h in headlines]
        
        datesources = [re.sub('\u200e', '', str(d.contents[0].contents[0])) for d in dates]
        
        hlines = [tagCleaner(h.a.contents) for h in headlines]
        
        for i in range(len(thumbs)):
            print(thumbs[i])
            print(hlinks[i])
            print(hlines[i])
            print(datesources[i])
        
        
        # for h in headlines:
        #     print(h.a['href'])
        #     print(tagCleaner(h.a.contents))
        #     print(type(h.a.contents[1])==bs4.NavigableString)
        #     print(str(h.a.contents[1]))
        
        # f = open(fname, 'w')
        
        # for s in stories:
        #     f.write(str(s) + "\n")
        
        # f.close()
        
    except Exception as e:
        print(e)
    finally:
        print("*"*25)

def readfromf(filename):
    f = open(filename, 'r')
    for l in f:
        print(l)
        


scraper(fullurl)

# readfromf(fname)