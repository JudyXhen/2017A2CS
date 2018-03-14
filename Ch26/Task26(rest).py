#Judith Chen S3C5
#Task 26/ 02 and 03

import pickle


class CarRecord :
	def __init__(self) :
		self.VehicleID = "BMW"
		self.Registration = ""
		self.DateOfRegistration = None
		self.EngineSize = 0
		self.PurchasePrice = 0.0
RECORDSIZE =len(pickle.dumps(CarRecord))
Car=[CarRecord() for i in range (5)]
i = int(input('Record Number? '))
if i!= 0 and i!=1 and i!=2 and i!=3 and i!=4:
	print("Invalid Input!")
else:
	while i !=5:
		Car[i].VehicleID = input('Vehicle ID: ')
		Car[i].Registration = input('Registration: ')
		Car[i].DateOfregistration =(input('Registration Date: '));
		Car[i].EngineSize = int(input('Engine size: '))
		Car[i].PurchasePrice = float(input('Purchase price: '))
		i = int(input('Next Record Number? Input 5 to end. '))

if i == 5:
	exit()
		
def InitialiseFile() :
	CarFile = open('CarFile.DAT','wb')
	for i in range(5): 
		Address = i * RECORDSIZE + 1
		CarFile.seek(Address, 0)
		pickle.dump(CarRecord(), CarFile)
	CarFile.close()
	

def Hash(reg) :
	result = ord(reg[0]) * RECORDSIZE + 1
	print('Hashed to ',result)
	return result

										   
def FindRecord(reg, CarFile) :
	Address = Hash(reg)
	CarFile.seek(Address, 0)
	ThisCar = pickle.load(CarFile) 
	return ThisCar
										   
def OutputData(ThisCar) :
	print(ThisCar.VehicleID) 
										   
def main() :
	InitialiseFile()
	Answer = input('find a record? (Y/N) ')
	while Answer != 'N' :
		Reg = input('Give vehicle registration: ')
		ThisCar = FindRecord(Reg, CarFile)
		OutputData(ThisCar)
		Answer = input('find a record? (Y/N) ')
	CarFile.close()
main()