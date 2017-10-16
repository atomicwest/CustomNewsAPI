'''

removes html tags from web-scraped data formatted that has been formatted
as strings

ex:

1. string input
s = "Suspect arrested following standoff at <b>Portland</b> motel"

tagCleaner(s)
#returns: Suspect arrested following standoff at Portland motel

2. list input

a = ['Suspect arrested following standoff at ', '<b>Portland</b>', ' motel']

tag-cleaner(a)
#returns: Suspect arrested following standoff at Portland motel


'''

import re
import bs4 

#use if all inputs  are strings OR lists of strings only
def tagCleaner(raw):
    out = ""
    if type(raw)==bs4.NavigableString:
        out = re.sub('<.*?>', '', str(raw))
        # out = re.sub(r'<.*?>', '', str(raw))
    elif type(raw)==list:
        for s in raw:
            line = str(s)
            if "<" in line:
                out+=re.sub('<.*?>', '', str(s))
            else:
                out+=line
    return out
    
    