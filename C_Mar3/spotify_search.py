import urllib
import json
impor sys

search_term = sys.argv[1]

url = "http://api.spotify.com/v1/search?"
params = urllib.urlencode({'q':search_term, 'limit':limit, 'type':'track'})
url = base_url
print url 

raw = urllib.urlopen(url).read()
data = json.loads(raw)

for track in data["tracks"]["items"]:
	print track ["name"], track["popularity"]