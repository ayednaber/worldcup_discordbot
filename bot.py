import os
import discord
from discord.ext.commands import Bot
from discord.ext import tasks
from datetime import datetime, timedelta, date
import json
import requests
# from boto.s3.connection import S3Connection

# from dotenv import load_dotenv
# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

dataDict = {'Argentina': 'đŚđˇ', 'Australia': 'đŚđş', 'Belgium': 'đ§đŞ', 'Brazil': 'đ§đˇ', 'Canada': 'đ¨đŚ', 'Switzerland': 'đ¨đ­', 'Cameroon': 'đ¨đ˛', 'Costa Rica': 'đ¨đˇ', 'Germany': 'đŠđŞ', 'Denmark': 'đŠđ°', 'Ecuador': 'đŞđ¨', 'Spain': 'đŞđ¸', 'France': 'đŤđˇ', 'Ghana': 'đŹđ­', 'Croatia': 'đ­đˇ', 'Iran': 'đŽđˇ', 'Japan': 'đŻđľ', 'Korea Republic': 'đ°đˇ', 'Morocco': 'đ˛đŚ', 'Mexico': 'đ˛đ˝', 'Netherlands': 'đłđą', 'Poland': 'đľđą', 'Portugal': 'đľđš', 'Qatar': 'đśđŚ', 'Serbia': 'đˇđ¸', 'Saudi Arabia': 'đ¸đŚ', 'Senegal': 'đ¸đł', 'Tunisia': 'đšđł', 'Uruguay': 'đşđž'}
dataDict['England'] = 'đ´ó §ó ˘ó Ľó Žó §ó ż'
dataDict['USA'] = 'đşđ¸'
dataDict['Wales'] = 'đ´ó §ó ˘ó ˇó Źó łó ż'

dataDict2 = {'đŚđˇ': 'Argentina', 'đŚđş': 'Australia', 'đ§đŞ': 'Belgium', 'đ§đˇ': 'Brazil', 'đ¨đŚ': 'Canada', 'đ¨đ­': 'Switzerland', 'đ¨đ˛': 'Cameroon', 'đ¨đˇ': 'Costa Rica', 'đŠđŞ': 'Germany', 'đŠđ°': 'Denmark', 'đŞđ¨': 'Ecuador', 'đŞđ¸': 'Spain', 'đŤđˇ': 'France', 'đŹđ­': 'Ghana', 'đ­đˇ': 'Croatia', 'đŽđˇ': 'Iran', 'đŻđľ': 'Japan', 'đ°đˇ': 'Korea Republic', 'đ˛đŚ': 'Morocco', 'đ˛đ˝': 'Mexico', 'đłđą': 'Netherlands', 'đľđą': 'Poland', 'đľđš': 'Portugal', 'đśđŚ': 'Qatar', 'đˇđ¸': 'Serbia', 'đ¸đŚ': 'Saudi Arabia', 'đ¸đł': 'Senegal', 'đšđł': 'Tunisia', 'đşđž': 'Uruguay'}
dataDict2['đ´ó §ó ˘ó Ľó Žó §ó ż'] = "England"
dataDict2['đşđ¸'] = 'USA'
dataDict2['đ´ó §ó ˘ó ˇó Źó łó ż'] = "Wales"

f = open('worldcupfixtures.json')
worldcupgames = json.load(f)

intents=discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
client = Bot(command_prefix='!', intents=intents)
# client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(str(client.user) + " has connected to Discord!")

@client.command()
async def sendmatches(ctx):
    general_channel = client.get_channel(1039966870226354248)
    radate = date.today()
    new_msg = ""
    datestr = ""

    # Here, we want to get the data every time we call the command
    worldcupdata = requests.get('https://fixturedownload.com/feed/json/fifa-world-cup-2022')
    for i in worldcupdata.json()[48:]:
        # print(i["DateUtc"][:len(i["DateUtc"]) - 1])
        date1 = datetime.strptime(i["DateUtc"][:len(i["DateUtc"]) - 1], '%Y-%m-%d %H:%M:%S')
        dateinjordan = date1 + timedelta(hours=3)
        dateintoronto = date1 - timedelta(hours=5)
        dateinmexico= date1 - timedelta(hours=6)
        dateineurope = date1 + timedelta(hours=1)
        message = ""
        if (radate == date1.date()):
            datestr += '**' + str(date1.date()) + '**\n'
            message += i["HomeTeam"] + ' ' + dataDict[i["HomeTeam"]] + " vs. " + i["AwayTeam"] + ' ' + dataDict[i["AwayTeam"]] + '\n'
            message += '**Times:** ' + dateinjordan.strftime('%I:%M %p') + " :flag_jo:" + "    " + dateineurope.strftime('%I:%M %p') + " :flag_eu:" + "     " + dateintoronto.strftime('%I:%M %p') +  " :flag_ca:" + "     " + dateinmexico.strftime('%I:%M %p') +  " :flag_mx:" + "\n \n"
        new_msg += message
    d = datestr.split("\n")
    todays_games = d[0] + "\n" + new_msg
    await general_channel.send(todays_games)

@client.command()
async def sendmatches2(ctx):
    general_channel = client.get_channel(1043884627246465034)
    radate = date.today()
    new_msg = ""
    datestr = ""

    # Here, we want to get the data every time we call the command
    worldcupdata = requests.get('https://fixturedownload.com/feed/json/fifa-world-cup-2022')
    for i in worldcupdata.json()[48:]:
        # print(i["DateUtc"][:len(i["DateUtc"]) - 1])
        date1 = datetime.strptime(i["DateUtc"][:len(i["DateUtc"]) - 1], '%Y-%m-%d %H:%M:%S')
        dateinjordan = date1 + timedelta(hours=3)
        dateintoronto = date1 - timedelta(hours=5)
        dateinmexico= date1 - timedelta(hours=6)
        dateineurope = date1 + timedelta(hours=1)
        message = ""
        if (radate == date1.date()):
            datestr += '**' + str(date1.date()) + '**\n'
            message += i["HomeTeam"] + ' ' + dataDict[i["HomeTeam"]] + " vs. " + i["AwayTeam"] + ' ' + dataDict[i["AwayTeam"]] + '\n'
            message += '**Times:** ' + dateinjordan.strftime('%I:%M %p') + " :flag_jo:" + "    " + dateineurope.strftime('%I:%M %p') + " :flag_eu:" + "     " + dateintoronto.strftime('%I:%M %p') +  " :flag_ca:" + "     " + dateinmexico.strftime('%I:%M %p') +  " :flag_mx:" + "\n \n"
        new_msg += message
    d = datestr.split("\n")
    todays_games = d[0] + "\n" + new_msg
    await general_channel.send(todays_games)


@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)
    if payload.channel_id == 1040452457521741904:
        role = discord.utils.get(guild.roles, name=dataDict2[payload.emoji.name])
        await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    guild = client.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)
    if payload.channel_id == 1040452457521741904:
        role = discord.utils.get(guild.roles, name=dataDict2[payload.emoji.name])
        await member.remove_roles(role)

@client.command()
async def test(ctx):
    general_channel = client.get_channel(1040452457521741904)
    print("I am here")
    msg = await general_channel.fetch_message(1043592750769111171)
    d = {'Argentina': 'đŚđˇ',
        'Belgium': 'đ§đŞ', 'Brazil': 'đ§đˇ', 'Canada': 'đ¨đŚ',
        'Germany': 'đŠđŞ',
        'Spain': 'đŞđ¸', 'France': 'đŤđˇ',
        'Croatia': 'đ­đˇ',} 
    d2 = {'đľđš': 'Portugal', 'đśđŚ': 'Qatar', ':england:': ':england:', 'đ¸đŚ': 'đ¸đŚ'}
    for i in d.values():
        await msg.add_reaction(i)
    
    for i in d2.keys():
        await msg.add_reaction(i)

@client.command()
async def delete(ctx,arg):
    await ctx.channel.purge(limit=int(arg))

@client.command()
async def time(ctx):
    testdatetime = datetime.today()
    await ctx.channel.send(str(testdatetime))

client.run(os.environ.get('DISCORD_TOKEN'))


# This is how to mention users
#   await general_channel.send(f"<@{i.id}> is the best")