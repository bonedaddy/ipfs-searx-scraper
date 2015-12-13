import requests
import json

url = 'https://searx.netzspielplatz.de'
data = []
index = ''

for i in range(1, 11):
    payload = {'q': 'site:ipfs.io/ipfs/', 'format': 'json', 'category_general': '1', 'pageno': i }
    r = requests.get(url, params=payload)

    list = r.json()

    del list[u'query']
    for x in list[u'results']:
        del x[u'engine']
        del x[u'engines']
        del x[u'url']
        del x[u'pretty_url']
        del x[u'host']
        del x[u'score']
        x[u'parsed_url'] = x[u'parsed_url'][2]

    stringlist = str(list).replace("{u'results': [", "").replace("]}", "").replace("{u", "{").replace(": u", ": ").replace(", u", ", ")

    data.append(stringlist)
    print "added page %d to data" % (i)

for item in data:
    index += ("%s, " % item)

f = open('idx.js', 'w')
index = index.rstrip(', ')
f.write('var pages = [' + index + ']')

print "wrote data to idx.js"

