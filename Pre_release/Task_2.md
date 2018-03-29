Task 2.3 
class Toy:
	def __init__(self,Name, num, p, a):
		self.__Name = ''
		self.__ID = num
		self.__Price = p
		self.__MinAge = a
	def GetName(self, Name):
		return self.__Name
	def GetID(self, num):
		return self.__ID
	def GetPrice(self, p):
		return self.__Price
	def GetMinAge(self, a):
		return self.__MinAge
	def SetName(self,Name):
		self.__Name = Name
	def SetID(self,num):
		self.__ID = num
	def SetPrice(self,p):
		self.__Price = p
	def SetMinAge(self,a):
		self.__MinAge = a
		if a < 0 or a > 18:
			print('Invalid')
		
Task 2.4
class ComputerGame(Toy):
	def __init__(self, Name, num, p, a, ca, co):
		Toy.__init__(self)
		self.__Category = ca
		self.__Console = co
	def GetCategory(self, ca):
		return self.__ca
	def GetConsole(self, co):
		return self.__co
	def SetCategory(self,ca):
		self.__Category = ca
	def SetConsole(self,co):
		self.__Console = co

class Vehicle:
	def __init__(self):
		Toy.__init__(self)
		self.__Type = ''
		self.__Height = 0
		self.__Length = 0
		self.__Weight = 0 
	def GetType(self):
		return self.__Type 
	def GetHeight(self):
		return self.__Height
	def GetLength(self):
		return self.__Length
	def GetWeight(self):
		return self.__Weight 
	def SetType(self,t):
		self.__Type = t
	def SetHeight(self,h):
		self.__Height = h
	def SetLength(self,l):
		self.__Length = l 
	def SetWeight(self,w):
		self.___Weight = w

Task 2.5
class Toy:
	def __init__(self,Name, num, p, a):
		Toy.SetName = (self, Name)
		Toy.SetID = (self, num)
		Toy.SetPrice = (self, p)
		Toy.SetMinAge = (self, a)
(Second part already in code. See line 22. )

Task 2.6
ToyInfo = []
ToyA = Vehicle()
vehicle.append('Red Sports Car','RSC13',15.00,6,'car',3.3,12.1,0.08)
Vehicle.append('14d','L4D01',10,15,'FPS','PC')
ToyA.SetName('Red Sports Car')
ToyA.SetID('RSC13')
ToyA.SetMiniAge(6)
ToyA.SetType('Car')
ToyA.SetHeight(3.3)
ToyA.SetLength(12.1)
ToyA.SetWeight(0.08)
ToyInfo.append(ToyA)

Task 2.7
def GetToy():
	for i in ToyInfo:
		if i.GetID == ID:
			print(self.__Name)
			print(self.__Price)
			print(self.__MinAge)
		else:
			print(‘doesnt exit or invalid)

Task 2.8
#assume no toy cost more than 100
def Discount(dsc):
	dsc = dsc/100
	for i in range(len(ToyInfo)):
		ToyInfo[i].Price = ToyInfo[i].Price * (1-dsc)

Task 2.9 
Bubble sort is a sorting algorithm that operates by going through the list to be sorted repeatedly while comparing pairs of elements that are adjacent.
Insertion sort is another sorting algorithm, which operates by inserting an element in the input list in to the correct position in a list (that is already sorted).

Task 2.10
#BubbleSort
def BubbleSort(GameInfo): 
	for i in range(len(GameInfo)):
		for j in range(i, len(GameInfo)):
			if GameInfo[i].GetPrice() > GameInfo[j].GetPrice():
				Temp = GameInfo[i]
				GameInfo[i] = GameInfo[j]
				GameInfo[j] = Temp
#InsertionSort










