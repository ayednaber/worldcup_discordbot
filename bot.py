import os
import discord
from discord.ext.commands import Bot
from discord.ext import tasks
from datetime import datetime, timedelta, date
import json

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

dataDict = {'Argentina': '🇦🇷', 'Australia': '🇦🇺', 'Belgium': '🇧🇪', 'Brazil': '🇧🇷', 'Canada': '🇨🇦', 'Switzerland': '🇨🇭', 'Cameroon': '🇨🇲', 'Costa Rica': '🇨🇷', 'Germany': '🇩🇪', 'Denmark': '🇩🇰', 'Ecuador': '🇪🇨', 'Spain': '🇪🇸', 'France': '🇫🇷', 'Ghana': '🇬🇭', 'Croatia': '🇭🇷', 'Iran': '🇮🇷', 'Japan': '🇯🇵', 'South Korea': '🇰🇷', 'Morocco': '🇲🇦', 'Mexico': '🇲🇽', 'Netherlands': '🇳🇱', 'Poland': '🇵🇱', 'Portugal': '🇵🇹', 'Qatar': '🇶🇦', 'Serbia': '🇷🇸', 'Saudi Arabia': '🇸🇦', 'Senegal': '🇸🇳', 'Tunisia': '🇹🇳', 'Uruguay': '🇺🇾'}
dataDict['England'] = '🏴󠁧󠁢󠁥󠁮󠁧󠁿'
dataDict['USA'] = '🇺🇸'
dataDict['Wales'] = '🏴󠁧󠁢󠁷󠁬󠁳󠁿'

dataDict2 = {'🇦🇷': 'Argentina', '🇦🇺': 'Australia', '🇧🇪': 'Belgium', '🇧🇷': 'Brazil', '🇨🇦': 'Canada', '🇨🇭': 'Switzerland', '🇨🇲': 'Cameroon', '🇨🇷': 'Costa Rica', '🇩🇪': 'Germany', '🇩🇰': 'Denmark', '🇪🇨': 'Ecuador', '🇪🇸': 'Spain', '🇫🇷': 'France', '🇬🇭': 'Ghana', '🇭🇷': 'Croatia', '🇮🇷': 'Iran', '🇯🇵': 'Japan', '🇰🇷': 'South Korea', '🇲🇦': 'Morocco', '🇲🇽': 'Mexico', '🇳🇱': 'Netherlands', '🇵🇱': 'Poland', '🇵🇹': 'Portugal', '🇶🇦': 'Qatar', '🇷🇸': 'Serbia', '🇸🇦': 'Saudi Arabia', '🇸🇳': 'Senegal', '🇹🇳': 'Tunisia', '🇺🇾': 'Uruguay'}
dataDict2['🏴󠁧󠁢󠁥󠁮󠁧󠁿'] = "England"
dataDict2['🇺🇸'] = 'USA'
dataDict2['🏴󠁧󠁢󠁷󠁬󠁳󠁿'] = "Wales"

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
    for i in worldcupgames[:48]:
        # print(i["DateUtc"][:len(i["DateUtc"]) - 1])
        date1 = datetime.strptime(i["DateUtc"][:len(i["DateUtc"]) - 1], '%Y-%m-%d %H:%M:%S')
        dateinjordan = date1 + timedelta(hours=3)
        dateintoronto = date1 - timedelta(hours=5)
        dateineurope = date1 + timedelta(hours=1)
        # print(radate)
        if (radate == date1.date()):
            message = '**' + str(date1.date()) + '**\n'
            message += i["HomeTeam"] + ' ' + dataDict[i["HomeTeam"]] + " vs. " + i["AwayTeam"] + ' ' + dataDict[i["AwayTeam"]] + '\n'
            message += '**Times:** ' + dateinjordan.strftime('%I:%M %p') + " :flag_jo:" + "    " + dateintoronto.strftime('%I:%M %p') + " :flag_ca:" + "     " + dateineurope.strftime('%I:%M %p') +  " :flag_eu:"
            await general_channel.send(message)

@client.command()
async def sendmatches2(ctx):
    general_channel = client.get_channel(1043884627246465034)
    radate = date.today()
    for i in worldcupgames[:48]:
        # print(i["DateUtc"][:len(i["DateUtc"]) - 1])
        date1 = datetime.strptime(i["DateUtc"][:len(i["DateUtc"]) - 1], '%Y-%m-%d %H:%M:%S')
        dateinjordan = date1 + timedelta(hours=3)
        dateintoronto = date1 - timedelta(hours=5)
        dateineurope = date1 + timedelta(hours=1)
        # print(radate)
        if (radate == date1.date()):
            message = '**' + str(date1.date()) + '**\n'
            message += i["HomeTeam"] + ' ' + dataDict[i["HomeTeam"]] + " vs. " + i["AwayTeam"] + ' ' + dataDict[i["AwayTeam"]] + '\n'
            message += '**Times:** ' + dateinjordan.strftime('%I:%M %p') + " :flag_jo:" + "    " + dateintoronto.strftime('%I:%M %p') + " :flag_ca:" + "     " + dateineurope.strftime('%I:%M %p') +  " :flag_eu:"
            await general_channel.send(message)


@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)
    role = discord.utils.get(guild.roles, name=dataDict2[payload.emoji.name])
    await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    guild = client.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)
    role = discord.utils.get(guild.roles, name=dataDict2[payload.emoji.name])
    await member.remove_roles(role)

@client.command()
async def test(ctx):
    general_channel = client.get_channel(1040452457521741904)
    print("I am here")
    msg = await general_channel.fetch_message(1043592750769111171)
    d = {'Argentina': '🇦🇷',
        'Belgium': '🇧🇪', 'Brazil': '🇧🇷', 'Canada': '🇨🇦',
        'Germany': '🇩🇪',
        'Spain': '🇪🇸', 'France': '🇫🇷',
        'Croatia': '🇭🇷',} 
    d2 = {'🇵🇹': 'Portugal', '🇶🇦': 'Qatar', ':england:': ':england:'}
    for i in d.values():
        await msg.add_reaction(i)
    
    for i in d2.keys():
        await msg.add_reaction(i)

@client.command()
async def delete(ctx,arg):
    await ctx.channel.purge(limit=int(arg))

@client.command()
async def go(ctx, arg):
    member = ctx.message.author
    discord.utils.get(member.server.roles, name=arg)

client.run('MTA0MDQ1NDM3OTEzMzc1MTMxNg.G82IIj.yKRa9FU-PoVODOOzHYoixUga-dbLVqb7LL92lQ')


# This is how to mention users
#   await general_channel.send(f"<@{i.id}> is the best")