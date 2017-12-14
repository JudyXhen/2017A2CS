#Judith Chen S3C5 O3
#Hash table

Key = 10
SearchKey = 10
HashTable = [1, 5, 10, 6, 7 ,4,6,2,4,3]

def Hash(Key):
	for n in range (0, 9):
		Adr = Key % (10)
	return Adr

def Insert(Key):
	i = Hash(Key)
	print('Checking index', i)
	while HashTable[i] != '' and i < 9:
		i = i+1 
		if i > len(HashTable):
			i = 1
		print('Checking index', i)
	HashTable[i] = Key
		
def FindRecord(SearchKey):
	i = Hash(SearchKey)
	print('Checking index', i)
	while (HashTable[i] != SearchKey) and HashTable[i] != '':
		i = i+1
		if i > len(HashTable):
			i = 0
		print('Checking index', i)
	while HashTable[i] != '':
		if HashTable[i] == SearchKey:
			print(i)
		return HashTable[i]
		
Insert(Key)
FindRecord(SearchKey)