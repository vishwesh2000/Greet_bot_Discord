# Welcome bot - Welcomes New members!
import discord

with open('token.txt','r') as token_file:
    token = token_file.readlines()[0]

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Welcoming Newbies🤪!!'))

GUILDID = Enter your guildid here
CHID = Enter your channelid here
@client.event
async def on_member_join(member):
    guild = client.get_guild(GUILDID)
    channel = guild.get_channel(CHID)
    await channel.send(f'Welcome to the server {member.mention}!! :partying_face::partying_face::partying_face:\nEnjoy your stay💯') #Welcoming on channel
    await member.send(f'Welcome to the {guild.name}, {member.name}! :partying_face:\nHead over to ,<#Enter your CHID here> for GAMING discussions🎮 and to <#Other CHID> for MUSIC🎼🎵..... Enjoy your stay💯') #Welcoming on DM

@client.event
async def on_message(message):
    if message.content == 'Mol!':
        await message.channel.send('Hi There!')
client.run(token)
