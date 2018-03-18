############# 3 b
class NodeClass:
	def __init__(self):
		self.__Data = ''
		self.__Pointer = -1
	
	def SetData(self, d):
		self.__Data = d
	
	def SetPointer(self, p):
		self.__Pointer  = 1
	
	def GetPointer(self, p):
		return self.__Pointer
		
############ 3 c
class QueueClass:
	def __init__(self):
		self.__Queue = [NodeClass for i in range (50)]
		self.__Head = -1
		self.__Tail = -1
		
############ 3 d
	def JoinQueue(self, d, i):
		if Head == -1:
			Head = 0
		self.__Tail = self.__Tail + 1
		i = self.__Tail
		self.__Queue[i].SetData(d)
		
		