import requests
import json
import random
import discord
#category codes are being stored..which are being used in the url to get questions 
linkdict={2:["genknowledge",9],3:["history",23],4:["mythology",20],5:["science-maths",19],6:["sports",21],7:["entertainment-videogames",15],8:["entertainment-anime_manga",31],9:["entertainment-television",14]}


def decode(str):#the question which we got from website were having some special characters in between charachters and words..so we had to decode it.
  while(str.find("&")!=-1):
    s1= str.find("&")
    s2=str.find(";")
    ss=str[s1:s2+1]
    str=str.replace(ss,"")
  return str
#json_data is a dictionary in which question i will be the key and [{question:"question"},correct answer="cor",wrong answer,etc] will be the value
def get_question(json_data,i):#gets a single question(in form of list which contains question and the options and correct option)
  qlist=[]#question
  oplist=[]#option list
  question=json_data['results']
  question=question[i]
  oplist.append(question['correct_answer'])
  oplist.extend(question['incorrect_answers'])
  oplist.sort()#to randomize the options..if we don't do this the correct answer will always be the 1st option
  for j in range(len(oplist)):#decoding the options 
    oplist[j]=decode(oplist[j])
  que=question['question']
  que=decode(que)#decoding the question
  qlist.append(que)
  qlist.extend(oplist)
  qlist.append(decode(question['correct_answer']))
  return qlist
  #print(question)
  '''
  Question
  
  Option1
  Option2
  Option3
  
  Correct answer
  '''
def get_trivia(msg):
  try :
    cat=int(str(msg.content).split(' ')[0])#getting the choice opted by user
    noq=int(str(msg.content).split(' ')[1])#getting the number of questions
    if cat>9:
      return "Give valid category(less than 11)"
    elif (noq>20 or noq<1):
      return "Give valid number of questions(1-20)"
  except Exception as message:
    return "Invalid request"
  
  if cat!=1:
    cat=linkdict[cat][1]#extracting the category code
    res=requests.get("https://opentdb.com/api_token.php?command=request")
    response= requests.get(f'https://opentdb.com/api.php?amount=20&category={cat}&token={res}')
    json_data=json.loads(response.text)
    if json_data['response_code']!=0:
      response=requests.get(f'https://opentdb.com/api.php?amount=20&category={cat}')
      json_data=json.loads(response.text)
  else:
    res=requests.get("https://opentdb.com/api_token.php?command=request")
    response= requests.get(f'https://opentdb.com/api.php?amount=20&token={res}')
    json_data=json.loads(response.text)
    if json_data['response_code']!=0:
      response=requests.get("https://opentdb.com/api.php?amount=20")
      json_data=json.loads(response.text)
  
  list=[]
  for i in range(noq):#add each question one by one to list
    qlist=get_question(json_data,i)
    list.append(qlist)
  return list#returning the list of question,options,correct option(to check whther the user gave correct answer)

  