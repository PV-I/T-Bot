import logging

#Hiding Logs (not important just debug stuff that nobody cares about)
logging.getLogger('discord').setLevel(logging.WARNING)
logging.getLogger('discord.http').setLevel(logging.WARNING)
logging.getLogger('discord.client').setLevel(logging.WARNING)
logging.getLogger('discord.gateway').setLevel(logging.WARNING)


import discord
import webbrowser
import colorama
from colorama import Fore, Style
colorama.init()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

ttr = False

@client.event
async def on_ready():
    print('Bot is active.\n')
    print('!tbot start ,to enable it!\n')
    print('!tbot stop ,to disable it!\n')
    colorama.init()

@client.event
async def on_message(message):
    if message.channel.id == dachannelidHERE: #da channel id
        global ttr

        if message.content == '!tbot start':
            if not ttr:
                ttr = True
                await message.channel.send('Scanning has started!')
                print(f'{Fore.GREEN}Scanning has started!{Style.RESET_ALL}')
        elif message.content == '!tbot stop':
            if ttr:
                ttr = False
                await message.channel.send('Scanning has stopped!')
                print(f'{Fore.RED}Scanning has stopped!{Style.RESET_ALL}')

        if ttr and message.content.startswith('https://www.roblox.com/catalog/'):
            link = message.content
            webbrowser.open(link)
            print(f'{Fore.YELLOW}Opened Roblox link: {link}{Style.RESET_ALL}')
#da bot token
client.run('dabottokenHERE')
