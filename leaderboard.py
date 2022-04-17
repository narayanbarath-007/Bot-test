from replit import db 
#This class represents the points table during a quiz
class pointstable:
  def __init__(self):
    self.dictionary={}
  def addpoints(self,name):
    if name in self.dictionary:
      self.dictionary[name]=self.dictionary[name]+1.0
    else:
      self.dictionary[name]=1.0
  def subpoints(self,name):
    if name in self.dictionary:
      self.dictionary[name]=self.dictionary[name]-0.5
    else:
      self.dictionary[name]=-0.5
  def printtable(self):
    l=[]
    for j in self.dictionary:
      l.append([j,self.dictionary[j]])
    return l
x=pointstable()


      