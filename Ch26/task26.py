#Task 26.01
#Judith Chen

import pickle

class CarRecord:	
	def __init__(self):
		self.VihicleID = ''
		self.Registration = ''
		self.DateOfRegistration = ''
		self.EngineSize = 0
		self.PurchasePrice = 0.0
		
CarA = CarRecord()
CarA.VihicleID = 'A1'
CarA.Registration = 'what'
CarA.DateOfRegistration = '180101'
CarA.EngineSize = 1
CarA.PurchasePrice = 100

CarB = CarRecord()
CarB.VihicleID = 'B1'
CarB.Registration = 'the'
CarB.DateOfRegistration = '180102'
CarB.EngineSize = 2
CarB.PurchasePrice = 200

CarC = CarRecord()
CarC.VihicleID = 'C1'
CarC.Registration = 'hell'
CarC.DateOfRegistration = '180103'
CarC.EngineSize = 3
CarC.PurchasePrice = 300

CarD = CarRecord()
CarD.VihicleID = 'D1'
CarD.Registration = 'are'
CarD.DateOfRegistration = '180104'
CarD.EngineSize = 4
CarD.PurchasePrice = 400

CarE = CarRecord()
CarE.VihicleID = 'E1'
CarE.Registration = 'those'
CarE.DateOfRegistration = '180105'
CarE.EngineSize = 5
CarE.PurchasePrice = 500
		
def NewFile():
	Records = []
	for i in range(5):
		Records.append(CarA)
		Records.append(CarB)
		Records.append(CarC)
		Records.append(CarD)
		Records.append(CarE)

def Save(Records):
	Records = open('Records.DAT','wb')
	for i in range(5):
		pickle.dump(Records[i],Records)
	Records.close()

def Load():
	RecordsFile = open('Records.DAT','rb')
	EoF = False
	while EoF == True:
		Records.append(pickle.load(Records))
	Records.close()
	return Records

def Output(Records):
	for i in range(5):
		print(Records[i].Registration)

def Main():
	ReadRecords = Load()
	Output(Records)
	Save(Records)
	
Main()
	
	
	
	
	
	
		