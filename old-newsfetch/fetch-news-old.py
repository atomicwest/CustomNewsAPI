from bs4 import BeautifulSoup as bsp
from urllib.request import urlopen, Request


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
        th          r
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
        
        stories = bsObj.findAll('div', {'class':'th'})
        # print(stories)
        
        f = open(fname, 'w')
        
        
        for s in stories:
            f.write(str(s) + "\n")
        
        f.close()
        
    except Exception as e:
        print(e)
    finally:
        print("*"*25)

def readfromf(filename):
    f = open(filename, 'r')
    for l in f:
        print(l)
        


scraper(fullurl)

readfromf(fname)