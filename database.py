from replit import db
#The levelcalculator calculates the level of a user
def levelcalculator(i):
  if i<0:
    #The level is 0 if score is negative
    return 0
  else:
    #The level is calculated according to the number of points of the user
    return(i//10+1)
#the below two functions get triggered when there is a change in 'level' of any 'user'
def levelup(name,level):#this function returns a string congratulating the user who has leveled up
  return f'Congratulations {name}, you have moved to level {level}'
def leveldown(name,level):#this function returns a string congratulating the user who has leveled down
  return f'Sorry {name}, you have been demoted to level {level}'
#This bot maintains 2 leader boards one is an Alltime leader board(it contains points of users for all the quizes plyed ) and other is a temporary one which resets for every quiz.
#So after every quiz is played it updates the Alltime leader board
def addtodb(l):#this function is to update the alltime leader board after a quiz is played
  levlist=[]#it contains all the strings of functions "levelup" and "leveldown"
  for j in l:
    x=1
    llcheck=0#a variable used to check whether any user is levelling up or down
    if "Lb" in db.keys():
      for i in range(len(db["Lb"])):
        if j[0] == db["Lb"][i][0]:
#logic to check for level up is get the remainder(when points of user divided by 10) and add to the points the user achieved in the round of trivia add check if it is above 10 or below 0
          llcheck=db["Lb"][i][1]%10
          llcheck=llcheck+j[1]          
          db["Lb"][i][1]=db["Lb"][i][1]+j[1]#updating the " user's " points
          db["Lb"][i][2]=levelcalculator(db["Lb"][i][1])#calculates the level for current points and updates the level in "Alltime Leader Board"
          if llcheck<0:#checking if the 'user' is levelled down
            levlist.append(leveldown(db["Lb"][i][0],db["Lb"][i][2]))
          elif llcheck>10:#checking if the 'user' is levelled up
            levlist.append(levelup(db["Lb"][i][0],db["Lb"][i][2]))
          x=0
          break
      if x==1:#if the "user" is playing for the first time..then this part get's executed
        j.append(levelcalculator(j[1]))
        db["Lb"].append(j)
    else:#if it's the first time executing "trivia"..then this part gets executed
      j.append(levelcalculator(j[1]))
      db["Lb"]=[j]
  return levlist#returns all the strings of functions "levelup" and "leveldown"
    
def PrintLb():#this function is to print the "All time leader board"...it returns a string containing all the info
  try:
    lbd=""
    for i in range(len(db["Lb"])):#it makes a string of all info of "Alltime Leader board"
      o= str(db["Lb"][i][0])#name of user
      p= str(db["Lb"][i][1])#points of user
      r=str(db["Lb"][i][2])#level of user
      lbd=lbd + "\n" + o + ":" + p + " level:" + r
    return lbd  
  except:
    print(db["Lb"])
    return "!"
def printrank(name):#this function is to print the rank of a user
  try:
    for i in range(len(db["Lb"])):#searching the user
      if db["Lb"][i][0]==name:
        return 'Level:'+str(db["Lb"][i][2])#returns the user level
    return "Invalid Username"
  except:
    return "Invalid Query"