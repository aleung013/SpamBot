import urllib
from bs4 import BeautifulSoup
import time


class Feed:
    ''' A Class to parse web pages to get updates'''
    def __init__(self, link, discord_channel, lastparsed=0):
        self.lastparsed = lastparsed
        self.webpage = link
        self.channel = discord_channel

    def parse_site(self):
        '''
        Parses site for new updates and returns the links to these updates
        '''
        page = urllib.request.urlopen(self.webpage)
        soup = BeautifulSoup(page, 'html.parser')
        tweets = soup.find_all('small', {'class':'time'}) # Get all tweets
        ctime = time.time()
        print(ctime, self.lastparsed)
        tweets = [tw for tw in tweets if int(tw.span['data-time']) > self.lastparsed] # Trim old content
        self.lastparsed = ctime
        paths = ['https://twitter.com' + tw.a['href'] for tw in tweets] # Get the link to all the tweets
        return paths
