#Judith Chen S3C5 O3
#Stacks

class Stack:
	def __init__(self):
		self.Value = ''
		self.NextPtr = -1
	
def InitStack():
	for a in range(10):
		Stacks = [Stack()]
	StackStart = -1
	FreePtr = 0
	for i in range(9):
		Stacks[i].NextPtr = i + 1
	Stacks[9].NextPtr = -1
	return (Stacks, StackStart, FreePtr)
		
		
def Push(Stacks, StartStack, FreePtr, Item):
	if FreePtr != -1:
		NewPtr = FreePtr
		Stacks[NewPtr].Value = Item
		FreePtr = Stacks[FreePtr].NextPtr
		Stacks[NewPtr].NextPtr = StartStack
	return(Stacks, StartStack, FreePtr)
	
def Pop(self):
	
		
	