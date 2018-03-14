#Task 26.01 Modified
#Judith Chen S3C5 Opt3

import pickle

class CarRecord:
	def __init__(self):
		self.VehicleID="BMW"
		self.Registration=""
		self.DateOfRegistration=None
		self.EngineSize=0
		self.PurchasePrice=0.00


Car=[CarRecord() for i in range (5)]

Car[0].EngineSize=1000
Car[1].EngineSize=2500
Car[2].EngineSize=2000
Car[3].EngineSize=2600
Car[4].EngineSize=3000
#print(Car[3].EngineSize)
i = int(input('Record Number? '))
if i!= 0 and i!=1 and i!=2 and i!=3 and i!=4:
	print("Invalid Input!")
else:
	while i !=5:
		Car[i].VehicleID = input('Vehicle ID: ')
		Car[i].Registration = input('Registration: ')
		Car[i].DateOfregistration =(input('Registration Date: '));
		#Car[i].EngineSize = int(input('Engine size: '))
		Car[i].PurchasePrice = float(input('Purchase price: '))
		i = int(input('Next Record Number? Input 5 to end. '))

CarFile=open('Cars.DAT','wb')


for i in range (5):
	pickle.dump(Car[i],CarFile)

CarFile.close()

CarFile=open('Cars.DAT','rb')
CarList=[]

for i in range(5):
	CarList.append(pickle.load(CarFile))
	   
CarFile.close()

j=int(input("Which car record do you want to output?"))

if j != 0 and j!=1 and j!=2 and j!=3 and j!=4:
	print("Invalid Input!")
else:
	print(CarList[j].VehicleID)
	print(CarList[j].Registration)
	print(CarList[j].DateOfRegistration)
	print(CarList[j].EngineSize)
	print(CarList[j].PurchasePrice)