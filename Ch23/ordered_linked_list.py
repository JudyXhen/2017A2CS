#Judith Chen S3C5 O3
#Linked List

class ListNode:
	def __init__(self):
		self.Value = None
		self.NextPtr = -1
	
class List:
	def __init__(self):
		self.FreePtr = 0
		self.StartPtr = -1
		self.Records = []
		
		NewNode = None
		for i in range(0,10):
			NewNode = ListNode()
			NewNode.NextPtr = i + 1
			self.Records.append(NewNode)
			NewNode.NextPtr = -1
			
	def Print():
		PrintList = List()
		for i in range(10):
			print(PrintList.Records[i])
			
	def InsertNode(List, StartPtr, FreePtr, NewItem):
		if FreePtr != -1:
			NewNodePtr = FreePtr
			List[NewNodePtr].Value = NewItem
			FreePtr = List[FreePtr].NextPtr
			PrevNodePtr = -1
			ThisNodePtr = StartPtr
			
			while ThisNodePtr != -1 and List[ThisNodePtr].Value < NewItem:
				PrevNodePtr = ThisNodePtr
				ThisNodePtr = StartPtr
			
			if PrevNodePtr == -1:
				List[NewNodePtr].NextPtr = StartPtr
				StartPtr = NewNodePtr
			else:
				List[NewNodePtr].NextPtr = List[PrevNodePtr].NextPtr 
				List[PrevNodePtr].NextPtr = NewNodePtr
				
	def FindNode(List, StartPtr, ToFindItem):
		CurrentNodePtr = StartPtr
		while CurrentNodePtr != -1 and List[CurrentNodePtr].Value != ToFindItem:
			CurrentNodePtr = List[CurrentNodePtr].NextPtr
			return(CurrentNodePtr)
	
	def DeleteNode(ToDeleteItem):
		ThisNodePtr = StartPtr
		while ThisNodePtr != -1 and List[ThisNodePtr].Value != ToDeleteItem:
			PrevNodePtr = ThisNodePtr
			ThisNodePtr = List[ThisNodePtr].NextPtr
		if ThisNodePtr != -1:
			if ThisNodePtr == StartPtr:
				StartPtr = List[StartPtr].NextPtr
			else:
				List[PrevNodePtr] = List[ThisNodePtr].NextPtr
			List[ThisNodePtr].NextPtr = FreePtr 
			FreePtr = ThisNodePtr
	
		
		
	
		
	