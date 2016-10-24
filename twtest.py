import urllib.request, urllib.error, urllib.parse
from twurl import augment

print('* Calling Twitter...')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
        {'screen_name': 'bhaumikbcg', 'count': '2'} )
print(url)
connection = urllib.request.urlopen(url)
data = connection.read().decode()
print(data)
headers = dict(connection.getheaders())
print(headers)
