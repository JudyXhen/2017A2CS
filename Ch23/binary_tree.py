#Judith Chen S3C5 O3
#Binary Tree

class TreeNode:
	def __init__(self):
		self.Data = ''
		self.LeftPtr = -1
		self.RightPtr = -1
		
def InitTree():
	Tree = [TreeNode() for i in range(8)]
	RootPtr = -1
	FreePtr = 0
	for i in range(7):
		Tree[i].LeftPtr = i+1
	return(Tree, RootPtr, FreePtr)
	
def InsertNode(Tree, RootPtr, FreePtr,NewItem):
	if FreePtr != -1:
		NewNodePtr = FreePtr
		FreePtr = Tree[FreePtr].LeftPtr
		Tree[NewNodePtr].Data = NewItem
		Tree[NewNodePtr].LeftPtr = -1
		Tree[NewNodePtr].LeftPtr = -1
		if RootPtr == -1: 
			RootPtr = NewNodePtr
		else: 
			ThisNodePtr = RootPtr
			while ThisNodePtr != -1:
				PrevNodePtr = ThisNodePtr
				if Tree[ThisNodePtr].Data > NewItem: 
					TurnedLeft = True
					ThisNodePtr = Tree[ThisNodePtr].LeftPtr
				elif Tree[ThisNodePtr].Data == NewItem:
					TurnedLeft = False
					Found = True
				else:
					TurnedLeft = False
					ThisNodePtr = Tree[ThisNodePtr].RightPtr
					
			if TurnedLeft == True:
				Tree[PrevNodePtr].LeftPtr = NewNodePtr
			else: 
				Tree[PrevNodePtr].RightPtr = NewNodePtr
	return Tree, RootPtr, FreePtr
				
def FindNode(Tree, RootPtr, FreePtr,SearchItem):
	SearchItem = int(input('search whats'))
	ThisNodePtr = RootPtr
	while ThisNodePtr != -1 and Tree[ThisNodePtr].Data != SearchItem:
		if Tree[ThisNodePtr].Data > SearchItem:
			ThisNodePtr = Tree[ThisNodePtr].LeftPtr
		else:
			ThisNodePtr = Tree[ThisNodePtr].RightPtr
	return ThisNodePtr

Tree, RootPtr, FreePtr = InitTree()
Tree, RootPtr, FreePtr = InsertNode(Tree, RootPtr, FreePtr, 8)
Tree, RootPtr, FreePtr = InsertNode(Tree, RootPtr, FreePtr, 12)
Tree, RootPtr, FreePtr = InsertNode(Tree, RootPtr, FreePtr, 22)
Tree, RootPtr, FreePtr = InsertNode(Tree, RootPtr, FreePtr, 2)
Tree, RootPtr, FreePtr = InsertNode(Tree, RootPtr, FreePtr, 1)
print(ThisNodePtr)
			
			
			
			
			
