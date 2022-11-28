import os
import discord
from discord.ext.commands import Bot
from discord.ext import tasks
from datetime import datetime, timedelta, date
import json
# from boto.s3.connection import S3Connection

# from dotenv import load_dotenv
# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

dataDict = {'Argentina': '🇦🇷', 'Australia': '🇦🇺', 'Belgium': '🇧🇪', 'Brazil': '🇧🇷', 'Canada': '🇨🇦', 'Switzerland': '🇨🇭', 'Cameroon': '🇨🇲', 'Costa Rica': '🇨🇷', 'Germany': '🇩🇪', 'Denmark': '🇩🇰', 'Ecuador': '🇪🇨', 'Spain': '🇪🇸', 'France': '🇫🇷', 'Ghana': '🇬🇭', 'Croatia': '🇭🇷', 'Iran': '🇮🇷', 'Japan': '🇯🇵', 'Korea Republic': '🇰🇷', 'Morocco': '🇲🇦', 'Mexico': '🇲🇽', 'Netherlands': '🇳🇱', 'Poland': '🇵🇱', 'Portugal': '🇵🇹', 'Qatar': '🇶🇦', 'Serbia': '🇷🇸', 'Saudi Arabia': '🇸🇦', 'Senegal': '🇸🇳', 'Tunisia': '🇹🇳', 'Uruguay': '🇺🇾'}
dataDict['England'] = '🏴󠁧󠁢󠁥󠁮󠁧󠁿'
dataDict['USA'] = '🇺🇸'
dataDict['Wales'] = '🏴󠁧󠁢󠁷󠁬󠁳󠁿'

dataDict2 = {'🇦🇷': 'Argentina', '🇦🇺': 'Australia', '🇧🇪': 'Belgium', '🇧🇷': 'Brazil', '🇨🇦': 'Canada', '🇨🇭': 'Switzerland', '🇨🇲': 'Cameroon', '🇨🇷': 'Costa Rica', '🇩🇪': 'Germany', '🇩🇰': 'Denmark', '🇪🇨': 'Ecuador', '🇪🇸': 'Spain', '🇫🇷': 'France', '🇬🇭': 'Ghana', '🇭🇷': 'Croatia', '🇮🇷': 'Iran', '🇯🇵': 'Japan', '🇰🇷': 'Korea Republic', '🇲🇦': 'Morocco', '🇲🇽': 'Mexico', '🇳🇱': 'Netherlands', '🇵🇱': 'Poland', '🇵🇹': 'Portugal', '🇶🇦': 'Qatar', '🇷🇸': 'Serbia', '🇸🇦': 'Saudi Arabia', '🇸🇳': 'Senegal', '🇹🇳': 'Tunisia', '🇺🇾': 'Uruguay'}
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
    new_msg = ""
    datestr = ""
    for i in worldcupgames[:48]:
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
    for i in worldcupgames[:48]:
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
    d = {'Argentina': '🇦🇷',
        'Belgium': '🇧🇪', 'Brazil': '🇧🇷', 'Canada': '🇨🇦',
        'Germany': '🇩🇪',
        'Spain': '🇪🇸', 'France': '🇫🇷',
        'Croatia': '🇭🇷',} 
    d2 = {'🇵🇹': 'Portugal', '🇶🇦': 'Qatar', ':england:': ':england:', '🇸🇦': '🇸🇦'}
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

# client.run(os.environ.get('DISCORD_TOKEN'))
client.run('MTA0MDQ1NDM3OTEzMzc1MTMxNg.Gr7vve.S-x6TpdkaBde930AQcxWCF-SrkaQYDmrH4YMSc')


# This is how to mention users
#   await general_channel.send(f"<@{i.id}> is the best")