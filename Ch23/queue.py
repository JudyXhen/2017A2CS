#Judith Chen
class Queues():
    def __init__(self,Value,Next):
        self.Value = Value
        self.Next = Next

class Queue():
    def __init__(self):
        self.FreePtr = -1
        self.StartPtr = -1
        self.PrevPtr = -1
        self.End = -1
        for i in range(1,10):
            self.Item = [Queues(None,i)]
        self.Item.append(Queues(None,-1))

    def Enqueue(self,Value):
        if self.FreePtr != -1:
            if self.StartPtr == -1:
                self.StartPtr = self.FreePtr
            Temp = self.Item[self.FreePtr].Next
            self.Item[self.FreePtr]= Queues(Value,-1)
            if self.PrevPtr != -1:
                self.Item[self.PrevPtr].Next = self.FreePtr
            self.PrevPtr = self.FreePtr
            self.FreePtr = Temp


    def Dequeue(self):
        if self.StartPtr != -1:
            TempPointer = self.FreePtr
            self.FreePtr = self.StartPtr
            self.StartPtr = self.Item[self.FreePtr].Next
            self.Item[self.FreePtr].Next = TempPointer
            return self.Item[self.FreePtr].Value





