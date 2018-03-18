#Chapter 27 questions
#Judith Chen S3C5 Option 3 

#----------Question 1----------#
1.a.
		Bank account
		^				^
		|				|
Personal account	Saving account
-----------------   ---------------

1.b.
class BankAccount:
	def __init__(self, num):
		self.__AccountHolderName = ''
		self.__IBAN = num
		
	def SetAccountHolderName(self,name):
		self.__AccountHolderName = name
		
	def GetAccountHolderName(self,name):
		return self.__AccountHolderName
		print(self.__AccountHolderName)
	
	def GetIBAN(self, num):
		return self.__IBAN
		print(self.__IBAN)

1.c.i
Personal account
- attributes
PaidFee
OverdraftLimit

- methods
SetLimit
PayFee
Overdraw

1.c.ii
SavingsAccount
- attributes
InterestAmount

- methods
CheckInterestRate
CalculateInterest

1.c.iii
encapsulation



#----------Question 2----------#
2. a. i
__________________________________
.SeasonTicketHolder.
	PRIVATE
	TicketHolderName: string
	TicketHolderEmail: string
--------
	PUBLIC
	GetName()
	GetEmail()
__________________________________
^								^
|								|
_____________________		______________________
.PayAsUGo.					.ContractTicketHolder.
	PRIVATE						PRIVATE
	Amount: Currency			FixedFee: Currency
---------					---------
	PUBLIC						PUBLIC
	GetAmount()					GetFee()
	UpdateAmount
_____________________		______________________

2. b. i.
Private methods are useful for debugging as it only functions in the class and won't be changed through other ways. 
2. b. ii
So they can be accessed anywhere in program. 

2. c. 
(I dont want the stupid name and address in book)
NewCustomer = ContractTicketHolder("Judith", "Judith@cs.a2", 10)

#----------Question 3----------#
3. a.
Containment

3. b. 
class NodeClass:
	def __init__(self):
		self.__Data = ''
		self.__Pointer = -1
	
	def SetData(self, d):
		self.__Data = d
	
	def SetPointer(self, p):
		self.__Pointer  = p
	
	def GetPointer(self, p):
		return self.__Pointer
		print(self.__Pointer)

3. c.
class QueueClass:
	def __init__(self):
		self.__Queue = [NodeClass for i in range (50)]
		self.__Head = -1
		self.__Tail = -1
		
3.d.
	def JoinQueue(self, d, i):
		if Head == -1:
			Head = 0
		self.__Tail = self.__Tail + 1
		i = self.__Tail
		self.__Queue[i].SetData(d)


















		