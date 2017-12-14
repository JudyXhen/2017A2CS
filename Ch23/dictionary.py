#Judith Chen S3C5 O3
#Dictionary

Keys = []
Values = []
Key = 'alu'
for i in range(10):
	Keys.append('')
	Values.append('')

def Insert(Key): 
	i = hash(Key) % 10
	Keys[i] = 'alu'
	Values[i] = 'arithmetic logic unit'

		
def Find(Key):
	i = hash(Key) % 10
	print('Checking index', i)
	while (Keys[i] != Key):
		i = i+1
	if i > len(Key):
		i = 0
		print('no record')
	if Keys[i] == Key:
		print('Found', Key, ':', Values[i])
		
Insert(Key)
Find(Key)
