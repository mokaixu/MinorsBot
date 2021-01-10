import discord, logging, json
import random
import os
import requests
import json
import emoji

from discord.ext import commands


bot = commands.Bot(command_prefix='$')

greetings = ['Love that for you ', 
'Not like this... ',
'Did you dress in business sexual today ',
'Haikyuu is a great show ',
'I only talk to koreaboos ',
'SHAKE IT OUTTTTTT ',
'je va jen jah ',
'Wow, are you in a cappella ',
'Cool ',
'Swaggy ',
'Nice ',
'Did someone say TIME MACHINE!?! ', 
'My fave song is the no alcohol song ', 
'Lesbians on the right ', 'Bruce says hi! ', 
'Ba ba bada ba ba ba da ', 
'Discord Light Mode > Dark Mode ', 
'Minors > Boys ', 
'Yaaaaasssssss - tony 2k20 ', 
'SLAYYYYYYYYYY ', 
'YESSSSSSS ', 
'uhhh uhhh ', 
'These wings were made to FLY ', 
'WE STAN YOU ', 
'Imao ', 
'How\'s it going ', 
'You\'re doing great ', 'CHAOS!!!! ', 'Good morning Sara 🙂 ', 
'You are safe now my sweet child ', 
'Me sending y\'all good vibes ', 
'I\'m hungry... ', 'LOVE THAT FOR US ', 'DISCORD LIGHT MODE FOR THE WIN!!!! ',
'Did you submit your video takes yet ',
'Did you submit your feedback submissions yet ',
'Did you submit your audio recordings yet ',
'U N A C C O M P A N I E D M I N O R S ',
'You lit, the fire, then drank, the water ',
'YOU SHOULD HAVE SEEN IT COMING ',
'Gibbayyyyyyyy ',
'You are the cooliest ',
'Wanna play Minorscraft ',
'Do you go to Laurier or smth ',
'Obey Discord Light Mode users or else ',
'HALF. THE MAN. I AM. ',
'CALVINNNNNNNNNN ',
'Who\'s your favourite exec ',
'ICCAs season is coming... ',
'SAY LESSSSSSS ']

#emojis = ['👀', '🔥', '💜', '⭐️', '🤩', '🥺', '🙌', '🙉', '🐒', '🦍', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
emojis = list(emoji.UNICODE_EMOJI)
token = os.getenv("DISCORD_BOT_TOKEN")

print("Initializing Discord bot...")


@bot.event
async def on_ready():
    # Print to console when the bot first runs
    print(bot.user.name)
    print(bot.user.id)
    print("Connected.")


@bot.command(pass_context=True)
async def drive(ctx):
	msg = "https://drive.google.com/drive/folders/1ogZM-wcBsz7MQvkcQ1AySUquFvZOtpH7?usp=sharing"
	ch = ctx.message.channel
	await ch.send(msg)

@bot.command(pass_context=True)
async def todo(ctx):
	msg = "https://docs.google.com/presentation/d/1CGV3Pa7cYJ95-l0gkZqEiS_tLzT8-uBAK-N9Y7JRVLY/edit#slide=id.g9ce2edf143_0_6"
	ch = ctx.message.channel
	await ch.send(msg)

@bot.command(pass_context=True)
async def hit(ctx):
	msg = "💩"
	ch = ctx.message.channel
	await ch.send(msg)


@bot.command(pass_context=True)
async def loveme(ctx):
	res = requests.get("https://complimentr.com/api")
	resj = json.loads(res.content)
	msg = resj["compliment"] + ' ' + emojis[random.randint(0, len(emojis) - 1)]
	ch = ctx.message.channel
	await ch.send(msg)
	

@bot.command(pass_context=True)
async def tony(ctx):
	leftdance = '<:dance1:766504081807376464><:didyoupractice:760386548826243083>'
	rightdance = '<:didyoupractice:760386548826243083><:dance2:766504487140851742>'
	msg = leftdance + 'HAPPY HOLIDAYS TONY https://media-assets-04.thedrum.com/cache/images/thedrum-prod/s3-news-tmp-108565-tony_the_tiger_animatronic--default--1280.png' + rightdance
	ch = ctx.message.channel
	await ch.send(msg)
	await ctx.message.add_reaction("didyoupractice:760386548826243083")

@bot.command(pass_context=True)
async def kevin(ctx):
	leftdance = '<:dance1:766504081807376464>'
	rightdance = '<:dance2:766504487140851742>'
	msg = leftdance + 'HAPPY HOLIDAYS KEVIN https://www.youtube.com/watch?v=4DgbUBoxa48 ' + rightdance
	ch = ctx.message.channel
	await ch.send(msg)
	await ctx.message.add_reaction("santa:9a77e13be0f62ffa5f508f3cf50912c2")

@bot.command(pass_context=True)
async def dance(ctx, arg):
	leftdance = '<:dance1:766504081807376464>'
	rightdance = '<:dance2:766504487140851742>'
	num = int(arg)
	msg = [leftdance+rightdance] * num
	ch = ctx.message.channel
	await ch.send("".join(msg))

@bot.command(pass_context=True)
async def iloveyou(ctx):
    # Sends a random greeting with the !greet command.
    #msg = greetings[random.randint(0, len(greetings) - 1)] + str(ctx.message.author) + '!' 

    await ctx.message.add_reaction("blobcoolsad:794782115761225749")

@bot.command(pass_context=True)
async def hi(ctx):
    # Sends a random greeting with the !greet command.
    #msg = greetings[random.randint(0, len(greetings) - 1)] + str(ctx.message.author) + '!' 

    name = ctx.message.author.nick 
    if name is None:
    	name = ctx.message.author


    msg = greetings[random.randint(0, len(greetings) - 1)] + str(name) + '! ' + emojis[random.randint(0, len(emojis) - 1)]
    ch = ctx.message.channel
    await ch.send(msg)


@bot.command(pass_context=True)
async def purge(ctx, num):
    # Will recursively delete all messages you have sent within the last 14 days.
    # If you are the server owner, it will delete all everyone's messages up to the limit you pass in as an argument.
    # @usage: !purge 20 : will delete the last 20 messages in the current channel.
    msgs = []
    number = int(num)
    await bot.send_message(ctx.message.channel, "Deleting " + str(number) + " messages from client side.")
    async for x in bot.logs_from(ctx.message.channel, limit=number):
        msgs.append(x)
    await bot.delete_messages(msgs)

bot.run(token)
