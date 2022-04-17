import discord
import os
import requests
import json
import random
from replit import db
from question import *
from leaderboard import pointstable as points
import database
import list_of_channels
import help
from forever import keep_alive
client=discord.Client()
@client.event
async def on_ready():
  print(f'{client.user} is ready')
first=True
@client.event
async def on_message(message):
  global first
  chi=message.channel.id
  chn=str(message.channel.name)
  msg=str(message.content)
  if message.author==client:#checks if the message was from itself and if yes does not take any action
    return 0
  if (first):#this is to let the user know how to get the info about the bot(will work only first time)
    await message.channel.send("Type !help to know information about me")
    first=False
  if message.content.startswith("!help"):#this is a command to get info about the bot
    await message.channel.send(help.Help())
  if message.content.startswith("!add"):#adds trivia to the channel (the channel,in which you are typing !add trivia)
    x=list_of_channels.AddChannel(message,chi)
    if x=="!":
      await message.channel.send("Invalid query")
    else:
      await message.channel.send(f'trivia is added to {x}')
  if message.content.startswith("!rem"):#removes trivia from the channel (the channel,in which you are typing !rem trivia)
    x=list_of_channels.RemChannel(message,chi)
    if x=="!":
      await message.channel.send("Invalid query")
    else:
      await message.channel.send(f'trivia is removed from {x}')
  if message.content.startswith("!hello"):
    await message.channel.send("Hi")
  if message.content.startswith("!trivia") :
    if (chi in db["Ch"]):#it checks whether the channel name(the user is typingthe command) has trivia or not
      menu="Options\n1.Any category\n2.General Knowledge\n3.History\n4.Mythology\n5.Mathematics\n6.Sports\n7.Video Games\n8.Japanese Anime and Manga\n9.Telivision"
      await message.channel.send(menu)#sends menu
      await message.channel.send('Give choice number of topic and number of questions(less than or equal to 20) with a space in between them')
      msg1 = await client.wait_for('message')#waits for users message(for choice and number of questions)
      triviarules=help.triviarules()#gets the rules of trivia
      await message.channel.send(triviarules)#sends the rules of trivia
      trivialist=get_trivia(msg1)#gets the list of questions(questions I mean list of question,options,correct option)
      if isinstance(trivialist,str)==True:
        await message.channel.send(trivialist)
      else:
        pt=points()
        n=int(str(msg1.content).split()[1])
        for i in range(n):
          questr="Question"+" "+str(i+1)
          await message.channel.send(questr)
          await message.channel.send(trivialist[i][0])
          await message.channel.send("Options:")
          opstr=""
          answer=trivialist[i][-1]
          for j in range(1,len(trivialist[i])-1):
            if answer==trivialist[i][j]:
              answer=chr(96+j)
            opstr=opstr+chr(96+j)+"."+trivialist[i][j]+"\n"
          await message.channel.send(opstr)
          msg = await client.wait_for('message')
          name=str(msg.author).split('#')[0]
          if msg.content.lower()==answer.lower():
            await message.channel.send(f'Answered Correctly by {name}')
            pt.addpoints(name)
            await message.channel.send("-"*80)
          else:
            await message.channel.send("Wrong Answer")
            await message.channel.send(f'Correct answer is {answer}')
            pt.subpoints(name)
            await message.channel.send("-"*80)
          await message.channel.send("Points Table:")  
          l=pt.printtable()
          for index in l:
            await message.channel.send(index[0]+":"+str(index[1]))
          await message.channel.send("-"*80)
        await message.channel.send("Game Over")
        await message.channel.send("-"*80)
        levellist=database.addtodb(l)
        for levelmsg in levellist:
          await message.channel.send(levelmsg)
#All time Leader Board is the Leader Board which stores the points across various quizzes 
  if message.content.startswith("!leaderboard"):
    if (database.PrintLb()=="!"):
      await message.channel.send("Invalid Query")
    else:
      await message.channel.send(database.PrintLb())#prints the "All time Leader Board"
  if message.content.startswith("!level"):
    name=msg.split(' ',1)[1]#gets the name(whose level is wanted by the user)
    await message.channel.send(database.printrank(name))
  
keep_alive()  
client.run(os.getenv("token"))

