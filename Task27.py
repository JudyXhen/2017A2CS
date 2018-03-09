#Task 27.02
#Judith Chen S3C5 Option3

import datetime
class LibraryItem:
	def __init__(self,t,a,i,bi):
		self.__Title = t
		self.__Author__Artist = a
		self.__ItemID = i
		self.__OnLoan = False
		self.__DueDate = datetime.date.today()
		self.__BorrowerID = bi
		
	def GetTitle(self):
		return(self.Title)
	
	def Borrowing(self, bi):
		self.__OnLoan = True
		self.__DueDate = self.__DueDate + datetime.timedelta(weeks = 3)
		self.__BorrowerID = bi
		
	def Returning(self):
		self.__OnLoan = False
		self.__BorrowerID = 0
	
	def PrintDetails(self):
		print(self.__Title, ';', self.__Author__Artist, ';', end = '')
		print(self.__ItemID, ';', self.__OnLoan) 
		print(self.__DueDate, '; Borrower:', self.__BorrowerID)
	

		
		
class Book(LibraryItem):
	def __init__(self,t,a,i,bi):
		LibraryItem.__init__(self, t, a, i,bi)
		self.__IsRequested = False
		self.__RequestedBy = 0
		
	def GetIsRequested(self):
		return (self.__IsRequested)
				
	def SetIsRequested(self):
		self.__IsRequested = True
		
	def PrintDetails():
		print('Book Details')
		LibraryIte.PrintDetails(self)
		print('Requested: ', self.__IsRequested)
	
	
class CD(LibraryItem):
	def __init__(self, t, a, i,bi):
		LibraryItem.__init__(self, t, a, i,bi)	
		self.__Genre = ''
		
	def GetGenre(self):
		return(self.__Genre)
		
	def SetGenre(self, g):
		self.__Genre = g
		
	def PrintDetails(self):
		print("CD Details")
		LibraryItem.PrintDetails(self)
		print(self.__Genre)

def main():
	Cd1 = CD('And Justice For All', 'Metallica', 1,123)
	Cd2 = CD('Dark Side of the Moon', 'Pink Floyd', 2,456)
	Cd3 = CD('Black Sabbath', 'Black Sabbath', 3,678)
	Cd4 = CD('Havana', 'CC', 4,789)
	Cd5 = CD('Rather Be', 'PTX', 5,890)

	Book1 = Book('12 Rules for Life', 'Jordan Peterson', 7,246)
	Book2 = Book('White Fang', 'Jack London', 2,357)
	Cd1.PrintDetails()


#27.03

class Borrower:
	def __init__(self, bn, ea, bi):
		self.__BorrowerName = bn
		self .__EmailAddress = ea
		self.__BorrowerID = bi
		self.__ItemsOnLoan = 0
		
	def GetBorrowerName(self):
		return (self.__BorrowerName)
		
	def GetEmailAddress(self):
		return (self.__EmailAddress)
		
	def GetBorrowerID(self):
		return (self.__BorrowerID)
	
	def GetItemsOnLoan(self):
		return (self.__ItemsOnLoan)
	
	def UpdateItemsOnLoan(self, iol):
		self.__ItemsOnLoan = self.__ItemsOnLoan + iol
		
	def PrintDetails(self) :
		print('Borrower is', self.__BorrowerName)
		print("ID is ", self.__BorrowerID) 
		print("email is", self.__EmailAddress)
		print("Items on loan: ", self.__ItemsOnLoan)



def Menu():
	print('1 - Add a new borrower')
	print('2 - Add a new book')
	print('3 - Add a new CD')
	print('4 - Borrow a book ')
	print('5 - Return a book')
	print('6 - Borrow a CD')
	print('7 - Return a CD ')
	print('8 - Request book')
	print('9 - Print all details')
	print('99 - Exit program')
	
	Finish = False
	NextBorrowerID = 1
	NextBookID = 1
	NextCD_ID = 1
	while Finish == False:
		Choice = int(input('What would you like to do?'))
		if Choice ==1: 
			BorrowerName = input('Name:')
			EmailAdd = input('EAddress:')
			BorrowerID = int(input('ID:'))
		elif Choice == 2:
			Title = input("Title: ")
			Author = input("Author: ")
			ItemID = NextBookID
			NextBookID = NextBookID + 1
			Book = Book(Title, Author, ItemID)
		elif Choice == 3:
			Title = input("Title: ")
			Artist = input("Artist: ")
			ItemID = NextCD_ID
			NextCD_ID = NextCD_ID + 1
			CD = T_CD(Title, Artist, ItemID)
		elif Choice == 4:
			BorrowerID = input("Borrower ID: ")
			ItemID = input("Book ID: ")
			Book.Borrowing(ItemID, Borrower)
		elif Choice == 5:
			BorrowerID = input("Borrower ID: ")
			ItemID = input("Book ID: ")
			Book.Returning(ItemID, Borrower)
		elif Choice == 6:
			BorrowerID = input("Borrower ID: ")
			ItemID = input("CD ID: ")
			CD.Borrowing(ItemID, Borrower)
		elif Choice == 7:
			BorrowerID = input("Borrower ID: ")
			ItemID = input("CD ID: ")
			CD.Returning(ItemID, Borrower)
		elif Choice == 8:
			BorrowerID = input("Borrower ID: ")
			ItemID = input("Book ID: ")
			Book.RequestBook(ItemID, Borrower)
		elif Choice == 9:
			print("Borrower Details")
			Borrower.PrintDetails()
			print("Book Details")
			Book.PrintDetails()
			print("CD Details")
			CD.PrintDetails()
		elif Choice == 99:
			Finish = True
			exit()
		
		else:
			print("wrong input")
	input()
Menu()
		


			
			
		
		