#Judith Chen S3C5


#Recursion 2
def groupSum(start, nums, target): 
	if target == 0:
		return True
	if start == len(nums):
		return False
	return (groupSum(start+1, nums, target-nums[start]) or groupSum(start + 1, nums, target))
print(groupSum(0, [2,4,8],9))

#groupSum6
def groupSum6(start, nums, target):
	if start >= len(nums): 
		return target == 0
	if nums[start] == 6:
		return groupSum6(start + 1, nums, target - nums[start])
	return groupSum6(start + 1, nums, target - nums[start]) or groupSum6(start + 1, nums, target)
print(groupSum6(0, [5, 6, 2], 8))

#groupNoAdj
def groupNoAdj(start, nums, target):
	if start >= len(nums):
		return target == 0
	return groupNoAdj(start + 2, nums, target - nums[start]) or groupNoAdj(start + 1, nums, target)
print(groupNoAdj(0, [2, 5, 10, 4], 12))

#groupSum5
def groupSum5(start, nums, target):
	if start >= len(nums): 
		return target == 0
	if nums[start] % 5 == 0:
		if (start < len(nums) - 1) and nums[start + 1] == 1:
			return groupSum5(start + 2, nums, target - nums[start])
		return groupSum5(start + 1, nums, target - nums[start])
	return groupSum5(start + 1, nums, target - nums[start]) or groupSum5(start + 1, nums, target)
print(groupSum5(0, [2, 5, 10, 4], 19))

#groupSumClump
def groupSumClump(start, nums, target):
	if start >= len(nums):
		return target == 0
 
	sum = nums[start]
	count = 1
	i = start + 1
	for i in range(len(nums)):
		if nums[i] == nums[start]:
			sum = nums[i] + 1
			count = count + 1 
	return (groupSumClump(start + count, nums, target - sum) or groupSumClump(start + count, nums, target))
print(groupSumClump(0, [2, 4, 4, 8], 14))

#splitArray
def splitArray(nums):
	index = 0
	sum1 = 0
	sum2 = 0
	return recArray(nums, index, sum1, sum2)

def recArray(nums, index, sum1, sum2 ):
	if index >= len(nums):
		return sum1 == sum2
	value = nums[index]
	return (recArray(nums, index + 1, sum1 + value, sum2) or recArray(nums, index + 1, sum1, sum2 + value))
print(splitArray([5, 2, 3]))

#splitOdd10
def splitOdd10(nums):
	index = 0
	sum1 = 0
	sum2 = 0
	return recArray(nums, index, sum1, sum2)

def recArray(nums, index, sum1, sum2):
	if index >= len(nums): 
		return (sum1%10 == 0 and sum2% 2 != 0) or (sum2%10 == 0 and sum1% 2 != 0)
	value = nums[index]

	return (recArray(nums, index + 1, sum1 + value, sum2) or recArray(nums, index + 1, sum1, sum2 + value))
print(splitOdd10([5, 5, 6, 1]))

#split53
def split53(nums):
	index = 0
	sum1 = 0
	sum2 = 0
	return recArray(nums, index, sum1, sum2)

def recArray(nums, index, sum1, sum2):
	if index >= len(nums):
		return sum1 == sum2
	value = nums[index]
	if (value % 5 == 0):
		return recArray(nums, index + 1, sum1 + value, sum2)
	elif (value % 3 == 0):
		return recArray(nums, index + 1, sum1, sum2 + value)
	else:    
		return (recArray(nums, index + 1, sum1 + value, sum2) or recArray(nums, index + 1, sum1, sum2 + value))
print(split53([1, 1]))














