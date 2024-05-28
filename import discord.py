import discord
import feedparser
import asyncio

# Token de votre bot Discord
TOKEN = 'votre_token'

# URL du flux RSS du subreddit "jeuxvideo"
RSS_FEED_URL = 'https://www.reddit.com/r/jeuxvideo/.rss'

# ID du channel où vous souhaitez envoyer les messages
CHANNEL_ID = ''

# Définition des intentions (intents)
intents = discord.Intents.default()

client = discord.Client(intents=intents)  # Passer les intentions comme argument nommé

# Définition des intentions (intents)
intents = discord.Intents.default()

client = discord.Client(intents=intents)  # Passer les intentions comme argument nommé

@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')

    # Récupérer le channel où envoyer les messages
    channel = client.get_channel(int(CHANNEL_ID))
    
    # Récupérer les articles du flux RSS
    feed = feedparser.parse(RSS_FEED_URL)
    for entry in feed.entries:
        await channel.send(entry.title + '\n' + entry.link)

@client.event
async def on_message(message):
    # Ne pas répondre à ses propres messages pour éviter une boucle infinie
    if message.author == client.user:
        return

client.run(TOKEN)