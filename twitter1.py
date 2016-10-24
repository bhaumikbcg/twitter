import urllib.request, urllib.error, urllib.parse
import twurl

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

while True:
    print('')
    acct = raw_input('Enter Twitter Account:')
    if ( len(acct) < 1 ) : break
    url = twurl.augment(TWITTER_URL,
        {'screen_name': acct, 'count': '2'} )
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    print(data[:250])
    headers = dict(connection.getheaders())
    # print(headers)
    print('Remaining', headers['x-rate-limit-remaining'])
