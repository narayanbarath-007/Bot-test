def Help():
  a="The query '!help' - prints information about me\n"
  b="1.!Hello - makes a bot say 'Hi'\n"
  c="2.!add trivia - adds trivia to the current channel.Don't forget to add trivia to your channel as you can't play in the channel without adding it\n"
  d="3.!rem trivia - removes trivia from the current channel\n"
  e="4.!trivia - prints the category menu, takes in category number and number of question as input to start the quiz\n"
  f="5.!leaderboard - prints the alltime leader board\n"
  g="6.!level 'username' - prints the level of 'username'\n"
  return a+b+c+d+e+f+g
def triviarules():
  a="Quiz Rules:\n"
  b="1.Only the first answer is taken.\n"
  c="2.There is no need to write the full answer. Option is enough.\n"
  d="3.Points scheme:\n"
  e="\t+1 - Correct Answer\n"
  f="\t-0.5 - Wrong Answer"
  return a+b+c+d+e+f
  