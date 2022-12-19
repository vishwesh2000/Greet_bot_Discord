#MUSIX SERVER WELCOMER and FUN BOT - MOLUCTUS
import discord

with open('token.txt','r') as token_file:
    token = token_file.readlines()[0]

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Welcoming Newbies🤪!!'))

@client.event
async def on_member_join(member):
    guild = client.get_guild(845535956135313418)
    channel = guild.get_channel(845535956135313420)
    await channel.send(f'Welcome to the server {member.mention}!! :partying_face::partying_face::partying_face:\nEnjoy your stay💯') #Welcoming on channel
    await member.send(f'Welcome to the {guild.name}, {member.name}! :partying_face:\nHead over to ,<#845535956135313421> for GAMING discussions🎮 and to <#845535956135313422> for MUSIC🎼🎵..... Enjoy your stay💯') #Welcoming on DM

@client.event
async def on_message(message):
    if message.content == 'Mol!':
        await message.channel.send('Helu Guru!!')
client.run(token)
