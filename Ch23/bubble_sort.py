#Bubble Sort 
#Judith Chen/ S3C5/ Option 3

Nums = [5,5,6,8,2,3,9,0]
Temp = 0

for i in range(len(Nums)-1):
	for j in range(len(Nums)-1):
		Temp = Nums[j+1]
		if Nums[j] > Nums[j+1]:
			Nums[j+1] = Nums[j]
			Nums[j] = Temp 
	i = i+1 
print(Nums)
	