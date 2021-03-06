# library for handling http request for Ushahidi API JSON data
import httplib

# store connection
conn = httplib.HTTPConnection("api.wolframalpha.com")
# pass values for API request to get JSON incidents list
conn.request("GET", "/v2/query?input=" + %s + "&appid=2ARWJK-68PPUGLUQY")
# actually get info, store in a variable
r1 = conn.getresponse()
# use read() to get data, store in variable
postsJSON = r1.read()

# try to import json library, if can't, import alternative simplejson
try:
    import json
except ImportError:
    import simplejson as json

# use json.loads() to parse the JSON data into something python-readable
postsParsed = json.loads(postsJSON)

# function to return "captions" from python-readable data.
def captions(posts):
    allCaptions = '' # Var to store the full list
    justPosts = postsParsed[u'response'][u'posts'] # Var to grab just the post objects
    for r in justPosts:
        allCaptions = allCaptions + r[u'caption']
    return allCaptions
