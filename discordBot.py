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



# @bot.command(pass_context=True)
# async def cat(ctx):
# 	msg = ["😹", "😻", "😿", "😽", "😺", "😼", "😾"]

# 	ch = ctx.message.channel
# 	await ch.send(msg)


@bot.command(pass_context=True)
async def cat(ctx):
	cat_emojis = ["😹", "😻", "😿", "😽", "😺", "😼", "😾"]
	res = requests.get("https://api.thecatapi.com/v1/images/search")
	res_url = res.json()[0]['url']
	# resj = json.loads(res.content)
	# print(resj)
	msg = res_url + ' ' + cat_emojis[random.randint(0, len(cat_emojis) - 1)]
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

# print("Loading Questions List...")
# questions = [];
# with open("questions.bot") as q:
# 	questions = q.readlines()
# print("Got {0} questions".format(len(questions)))
# print("Done.")
# ########################
# ### HELPER FUNCTIONS ###
# ########################
# def isUserServerOwner(usr):
# 	usrServer = usr.server
# 	serverOwner = usrServer.owner
# 	if (usr == serverOwner):
# 		return True
# 	return False

# def isUserServerOwner_Check(ctx):
# 	usr = ctx.message.author
# 	return isUserServerOwner(usr)

# # This checks if the user has the role specified by the 'AdminRole' property or is the server owner
# def isUserAdministrator(usr):
# 	# First check to see if the user has the admin role
# 	adminRole = bc.getProperty('AdminRole')
# 	userRoles = (r for r in usr.roles)
# 	try:
# 		return ((adminRole in userRoles) or isUserServerOwner(usr))
# 	except:
# 		print("An uncaught exception has occurred")
# 		return False
# 	return False

# def isUserAdministrator_Check(ctx):
# 	usr = ctx.message.author
# 	return isUserAdministrator(usr)

# # This checks if the user has the role specified by 'ModRole' property
# def isUserModerator(usr):
# 	modRole = bc.getProperty('ModRole')
# 	userRoles = (r for r in usr.roles)
# 	try:
# 		return ((modRole in userRoles) or isUserAdministrator(usr))
# 	except:
# 		print("An uncaught exception has occurred.")
# 		return False
# 	return False

# def isUserModerator_Check(ctx):
# 	usr = ctx.message.author
# 	return isUserModerator(usr)

# async def postModReport(event, reason, msg):
# 	modChan = bc.getProperty('ModReportChannel')
# 	report = "MOD EVENT: {0}.\nREASON: {1}.\n```{2}```".format(event, reason, msg)
# 	try:
# 		await bot.send_message(modChan,report)
# 	except:
# 		print("Could not post to mod channel!")

# ##################
# ### BOT EVENTS ###
# ##################
# @bot.event
# async def on_ready():
# 	print('------')
# 	print('Logged in as {0} (ID: {1})'.format(bot.user.name,bot.user.id))
# 	print('------')

# ######################
# ### ADMIN COMMANDS ###
# ######################
# @bot.command(pass_context=True)
# @commands.check(isUserAdministrator_Check)
# async def setModRole(ctx, r : discord.Role):
# 	usr = ctx.message.author
# 	bc.setProperty('ModRole',r)
# 	await bot.say("Moderator Role set to: {0} ({1})".format(r.name,r.id))

# @bot.command(pass_context=True)
# @commands.check(isUserAdministrator_Check)
# async def setModReportChannel(ctx, chan : discord.Channel):
# 	bc.setProperty("ModReportChannel", chan)
# 	await bot.say("Mod Events will be reported to: {0}.".format(chan.name))

# ######################
# ### Question Setup ###
# ######################

# # This sets what channel the questions should be posted to.
# @bot.command(pass_context=True)
# @commands.check(isUserModerator_Check)
# async def setQuestionChannel(ctx, chan : discord.Channel):
# 	bc.setProperty("QuestionChannel", chan)
# 	await bot.say("Questions will be posted to: {0}.".format(chan.name))

# # Takes the time to post a question as a 24 hour string, I.E "13:00" for 1 PM, "16:30" for 4:30 PM, etc.
# # Note: The time periodic checker only has a resolution of 10 minutes, so the exact moment of execution is only precise to within that.
# @bot.command()
# @commands.check(isUserModerator_Check)
# async def setRotateTime(hhmm):
# 	try:
# 		comps = hhmm.split(":")
# 		theTime = dt.time(hour=int(comps[0]),minute=int(comps[1]))
# 	except:
# 		await bot.say("There was a problem interpreting your string as a time")
# 		return;
# 	bc.setProperty("RotateTime",theTime)
# 	await bot.say("A new question will be posted every day at {0}".format(theTime))
# 	await postModReport("Question Rotate Time Changed", "setRotateTime command called", "New Time: {0}".format(theTime))

# async def checkSchedule():
# 	nowTimeFull = dt.datetime.now();
# 	nowTime = dt.time(hour=nowTimeFull.hour,minute=nowTimeFull.minute,second=nowTimeFull.second)
# 	lastCheck = bc.getProperty("LastCheckTime")
# 	rotateTime = bc.getProperty("RotateTime");
# 	doQuestions = bc.getProperty("DoQuestions")
# 	if (rotateTime is not None and doQuestions is True):
# 		# The last check is a catch for if the rotate time is somewhere near midnight by evaluating to true if we last ran the scheduler "After" the current time (I.E 23:55 -> 00:05)
# 		if (nowTime >= rotateTime and (lastCheck < rotateTime or lastCheck >= nowTime)):
# 			await doRotateQuestion()
# 	# Now schedule the next check
# 	bc.setProperty("LastCheckTime",nowTime);
# 	await asyncio.sleep(600) # Wait 10 minutes for the next check
# 	theTask = asyncio.ensure_future(checkSchedule())

# async def doRotateQuestion():
# 	qchan = bc.getProperty("QuestionChannel")
# 	if (qchan is not None):
# 		await bot.purge_from(qchan,limit=10000)
# 		num = rnd.randint(len(questions));
# 		if (num == bc.getProperty("LastNum")):
# 			if (num < len(questions)-1):
# 				num = num+1;
# 			else:
# 				num = num-1;
# 		bc.setProperty("LastNum",num)
# 		await bot.send_message(qchan,questions[num])
# 		await postModReport("Question Rotated (Next ID: {0})".format(num), "Rotation Time reached ({0})".format(bc.getProperty("RotateTime")),questions[num])


# # These next two just start and stop the question rotations. Starting starts the "doRotate()" function which continually calls itself in a non-blocking manner (I.E The previous invocation exits as soon as the next one is called, so we don't get an infinite pile of blocked functions)
# # The questions are started by calling doRotate() on another thread, which in turn keeps calling itself indefinitely. The prefs class keeps a handle on the current running/waiting task so it can be killed if needed.
# # The questions are stopped by calling cancel() on the currently running/waiting async task. This will kill the task even if it's currently sleeping.
# @bot.command()
# @commands.check(isUserModerator_Check)
# async def startQuestions():
# 	rtime = bc.getProperty("RotateTime")
# 	if (rtime is None):
# 		await bot.say("WARNING: A rotation time has not been set. Defaulting to 00:00 (Midnight)")
# 		midnight = dt.time() # Defaults to 00:00
# 		await setRotateTime("00:00")
# 	qchan = bc.getProperty("QuestionChannel");
# 	if (qchan is None):
# 		await bot.say("WARNING: A question channel has not been set. Questions may not be posted.")
# 	bc.setProperty("DoQuestions",True);
# 	await postModReport("Question Rotation Starting", "Question rotation start command used.", "Questions started")

# @bot.command()
# @commands.check(isUserModerator_Check)
# async def stopQuestions():
# 	bc.setProperty("DoQuestions",False)
# 	await postModReport("Question Rotation Stopping", "Question rotation stop command used", "Questions stopped.")

# # Everything's good. Let's go!
# print("Starting task scheduler...")
# asyncio.ensure_future(checkSchedule())
# print("Done.")

bot.run(token)
