#Judith Chen 

###########Define everything
import random
Words = [[]]
QuesLib = ['what', 'why', 'where', 'how', 'who', 'when', 'am', 'is', 'are', 'could', 'would', 'will', 'can', 'do', 'does', 'have']
AnsLib = ['Dont be on it.', 'Of course.', 'Be bold.', 'Tell someone what it means to you.', 'You will have to compromise.', 'Be delightfully sure of it.', 'You will get a positive result.', 'Prepare for the unexpected', 'A strong commitment will achieve good results.', 'Gentle persistence will pay off.']


############FUNCTION
def SetUpGame():   #Start the game
	print('Type Enter to begin and to continue.')
	input()
	print('Hello there.')
	input()
	print('You come with a question, do you?')
	input()
	print('I am the program that you exactly need. I can answer every question, and guide you through your life.')
	input()
	print('Lets begin.')
	input()
	EnterQuestion()


def Exit():
	c = input('whether you want to continue or not. type y shows continue,n shows over.')
	if   c == 'y':
	     EnterQuestion()
	elif c == 'n':
	     print('The end.')
	else:
	     print('error, please rewrite.')
	     Exit()
	
def EnterQuestion():
	Input = str(input('Ask whatever you want: '))
	Ques = Input.lower()
	x = 0
	for i in range(len(Ques)):
		if Ques[i] == " ":
			Words.append([])
			x = x+1
		else:
			Words[x].append(Ques[i])
	print('Ready for the anwer?')
	input()
	GiveAnswer()
			
def GiveAnswer():
	Answer = random.randint(0,9)
	print(AnsLib[Answer])

SetUpGame()			
	
	
	