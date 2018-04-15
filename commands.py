import discord
import asyncio
from constants import *
import random

from feeds import Feed

feeds = []

# Parses and Runs the command
# Returns a string for the bot to output after running the command
def run_command(message):
    # Parse message
    content = message.content
    channel_mentions = message.channel_mentions
    print(content)
    content = content[len(Prefix):] # Remove trailing newline
    content = content.split(Delim) # Split by delim
    command = content[0]
    params = content[1:]

    retstr = ''
    embed = None
    if command == 'help':
        retstr = helpmessage(params)
    elif command == 'rand':
        retstr = str(rand(params))
    elif command == 'flip':
        retstr = flip(params)
    elif command == 'addfeed':
        retstr = add_feed(params, channel_mentions)
    else:
        retstr = Message_Unknown_Command
    print(retstr)
    return retstr, embed



def helpmessage(params):
    '''
    Prints out a help message.
    If a command is given, prints out detailed description of the command.
    Params: [commands]:string - Represents the command to be looked up
    '''
    retstr = ''
    if len(params) == 0:
        retstr = Message_Help
    else:
        command = params[0]
        if command == 'help':
            retstr = Message_Help_Help
        elif command == 'rand':
            retstr = Message_Help_Rand
        elif command == 'flip':
            retstr = Message_Help_Flip
        else:
            retstr = Message_Unknown_Command
    return retstr
            
def rand(params):
    '''
    Returns a random integer within given range [lo,hi] inclusive
    Params: [x]:int - Represents the lo of the range, or hi if only x is given. Default 1
            [y]:int - Represent the hi of the range. Default 100
    '''
    lo, hi = 1, 100
    if len(params) == 1:
        lo, hi = 1, int(params[0])
    elif len(params) == 2:
        lo, hi = int(params[0]), int(params[1])

    ret = random.randint(lo,hi) # Get random integer
    return ret


def flip(params):
    '''
    Flips a coin and returns the output
    Params - [weight]:float [0,1] - Represents how often heads should appear. Default .5
    '''
    
    weight = 0.5
    if len(params) == 1:
        weight = float(params[0])
        
    roll = random.random() # Roll a random number
    ret = 'Heads!'
    if roll > weight:
        ret = 'Tails!'
    return ret

async def grab_feeds(client):
    '''
    Check all feeds for updates and post updates in respective channels
    '''
    await client.wait_until_ready()
    global feeds
    while not client.is_closed:
        for feed in feeds:
            print('Scraping',feed.webpage)
            links = feed.parse_site()
            for link in links:
                await client.send_message(feed.channel, link)
        await asyncio.sleep(Feed_Sleep_Time)
    

def add_feed(params, channel_mentions):
    '''
    Add feed to be check for updates, which will be posted to specificed channel
    Params: feed - Website that will be parsed for updates
            channel - Discord channel where updates will be posted
    '''
    feed = params[0]
    channel = channel_mentions[0]
    global feeds
    feed = Feed(feed, channel)
    feeds.append(feed)
    return Message_Successful_Add_Feed
