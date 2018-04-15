import discord
import asyncio
import sys
import commands

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

@client.event
async def on_message(message):
    # Ignore messages from this bot
    if message.author == client.user:
        return
    # Find command
    if message.content.startswith(commands.Prefix):
        out_message = commands.run_command(message)
        if out_message != '':
            await client.send_message(message.channel, out_message)
    
if __name__ == '__main__':
    client.run(sys.argv[1])
    
