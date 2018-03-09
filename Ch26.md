#Judith Chen/ S3C5/ Option 3
#Chapter 26 Questions


1.
a.
i.
class CustomerRecord:
	def __init__:
		self.CustomerID = 0
		self.CustomerName = ‘’
		self.CustomerPhone = ‘’
		self.TotalOrders = 0

ii. 
CustomerData = []
for i in range (1000): 
	CustomerData.append(CustomerRecord)

b.
i.
def Hash(CustomerID):
	Address = CustomerID % 1000
	return Address

ii.
def AddRecord(//CustomerData, Customer):
	Position = Hash(CustomerID)//Customer.CustomerID
	if CustomerData[Position] == "":
		CustomerData[Position].append(CustomerRecord())// = Customer
	else: 
		Position = Position + 1
		AddRecord()

iii.
def FindRecord(CustomerID, CustomerData):
	Address = Hash(ID)
	while CustomerData[Address] != CustomerID:
		Address = Address +1
	print(Address)
	return (Address)

c. 
import pickle
def SaveData(CustomerData) :
	CustomerFile = open('CustomerData.Dat','wb')
	for i in range(1000) :
		pickle.dump(CustomerData[i], CustomerFile)
	CustomerFile.close()

d. 
import pickle
CustomerData = []
for i in range (1000): 
	CustomerData.append(CustomerRecord)

def Hash(CustomerID):
	Address = CustomerID % 1000
	return Address

def AddRecord(//CustomerData, Customer):
	Position = Hash(CustomerID)//Customer.CustomerID
	if CustomerData[Position] == "":
		CustomerData[Position].append(CustomerRecord())// = Customer
	else: 
		Position = Position + 1
		AddRecord()

def FindRecord(CustomerID, CustomerData):
	Address = Hash(ID)
	while CustomerData[Address] != CustomerID:
		Address = Address +1
	print(Address)
	return (Address)

def SaveData(CustomerData) :
	CustomerFile = open('CustomerData.Dat','+ab')
	for i in range(1000) :
		pickle.dump(CustomerData[i], CustomerFile)
	CustomerFile.close()
	

2.
def OpenFile() :
	FileName = input("Which file do you want to use? ")
try:
	Channel = open(FileName, 'rb+')
except :
	print("File does not exist")




	