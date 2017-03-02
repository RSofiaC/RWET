import urllib
import json
impor sys

search_term = sys.argv[1]

url = "http://api.spotify.com/v1/search?q=" +search_term + "&type=track"

raw = urllib.urlopen(url).read()
data = json.loads(raw)

for track in data["tracks"]["items"]:
	print track ["name"]