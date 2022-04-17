#this file is to control whether the 'trivia' works in a particular channel or not 
from replit import db
#this function is to add 'trivia' to a particular channel which enables you to play trivia in that channel
#used 'try' and 'except' in both functions to avoid getting errors when users give invalid queries
#'db["Ch"]' is the list of all channel ids that user can play 'trivia'
def AddChannel(m,chi):# 'm' is the message and 'chi' is the channel id 
  try:
    t=str(m.content).split(' ')[1]#t gets the second word of the query
    if t=="trivia":#checks if the second word of query is trivia
      if "Ch" in db.keys():
        y=db["Ch"]
        y.append(chi)
        db["Ch"]=y
      else:
        db["Ch"]=[chi]
      return str(m.channel.name)#returns channel name
    else:
      return "!"
  except:
    return "!"
#this function is to remove 'trivia' from a particular channel, when removed 'trivia' can't be played in that channel until added    
def RemChannel(m,chi):# 'm' is the message and 'chi' is the channel id
  try:
    t=str(m.content).split(' ')[1]
    if t=="trivia":
      if "Ch" in db.keys():
        y=db["Ch"]
        y.remove(chi)
        db["Ch"]=y
        return str(m.channel.name)##returns channel name
      else:
        return "!"
    else:
      return "!"
  except:
    return "!"
