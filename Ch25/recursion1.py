#### Judith Chen/ S3C5/ Option-3 
#### Solutions to CodingBat Recursion1 

#Factorial
def Factorial(n):
	if n == 1: 
		return 1
	return n * Factorial(n-1)
print(Factorial(6))

#Bunny Ears
def BunnyEars(bunnies):
	if bunnies == 0:
		return 0
	return BunnyEars(bunnies-1) + 2
print(BunnyEars(4))

#Fibonacci
def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	print (fibonacci(n-1) + fibonacci(n-2))
fibonacci(2)

#bunnyEars2
def bunnyEars2(bunnies):
	if bunnies == 0:
		return 0
	if bunnies % 2 == 1:
		return (2 + bunnyEars2(bunnies - 1))
	print (3 + bunnyEars2(bunnies - 1 ))	
bunnyEars2(2)

#triangle
def triangle(rows):
	if rows == 0:
		return 0
	return (rows + triangle(rows-1))
print(triangle(2))

#sumDigits
def sumDigits(n):
	if n == 0:
		return 0
	return ((n % 10) + sumDigits(n//10))
print(sumDigits(126))

#count7
def count7(n):
	if n < 1:
		return 0;
	if n % 10 == 7: 
		return 1 + count7(n//10)
	else:
		return count7(n//10)
print(count7(717))

#count8: failed to count twice...
def count8(n): 
	if n == 0:
		return 0
	if (n % 10) == 8:
		return (1 + count8(n//10))
	if(n / 10 % 10 == 8):
		return (1 + count8(n//10))
	return count8(n//10)
print (count8(8188))

#powerN
def powerN(base,n):
	if n == 0 or base == 1:
		return 1
	if base == 0: 
		return 0
	return base*powerN(base, n-1)
print(powerN(3, 3))

#countX
def countX(str):
	if len(str) == 0:
		return 0
	if str[0]== 'x':
		return (1 + countX(str[1:]))
	else:
		return (0 + countX(str[1:]))
print(countX('xx'))

#countHi
def countHi(str):
	if len(str) < 2:
		return 0
	if str[0] == 'h' and str[1] == 'i':
		return (1 + countHi(str[2:]))
	else:
		return (0 + countHi(str[2:]))
print(countHi('hihihi'))

#changeXY
def changeXY(str):
	if len(str) == 0:
		return ''
	if str[0] == 'x':
		return ('y' + changeXY(str[1:]))
	else:
		return (str[0] + changeXY(str[1:]))
print(changeXY('codex'))

#changePi
def changePi(str):
	if len(str) == 0:
		return ''
	if str[0] == 'p' and str[1] == 'i':
		return ('3.14' + changePi(str[2:]))
	else:
		return (str[0] + changePi(str[1:]))
print(changePi('xpixx'))

#noX
def noX(str):
	if len(str) == 0:
		return ''
	if str[0] == 'x':
		return ('' + noX(str[1:]))
	else:
		return (str[0] + noX(str[1:]))
print(noX('xaxb'))

#array6
def array6(nums,index):
	if len(nums) == 0:
		return False
	if nums[index] == 6:
		return True
	elif index < len(nums)-1:
		return (array6(nums, index+1))
	else:
		return False
print(array6([1,6,7], 0))

#array11
def array11(nums, index):
	if index >= len(nums):
		return 0
	if nums[index] == 11:
		return (1 + array11(nums,index + 1))
	else:
		return array11(nums,index + 1)
print(array11([1, 2, 3, 4], 0))

#array220
def array220(nums, index):
	if index >= len(nums) - 1:
		 return False
	if nums[index + 1] == nums[index] * 10:
		 return True
	return array220(nums, index + 1)
print(array220([1, 2, 20], 0))

#allStar (has a bug
def allStar(str):
	if len(str) < 1:
		return ''
	else:
		return (str[0] + '*' + allStar(str[1:]))
print(allStar('hello'))

#pairStar
def pairStar(s):
	if (len(s) <= 1): 
		return s
	else:
		if (s[0] == s[1]):
			return s[0] + "*" + pairStar(s[1:])
		else:
			return s[0] + pairStar(s[1:])

#endX: RecursionError: maximum recursion depth exceeded in comparison
def endX(str):
	if str == '':
		return ''
	if str[0] == 'x':
		return endX(str[1:] + 'x')
	else:
		return str[0] + endX(str[1:])
#print(endX("xhixhix"))


#countPairs
def countPairs(str):
	if len(str) < 3:
		return 0
	if str[0] == str[2]:
		return (1 + countPairs(str[1:]))
	else:
		return (0 + countPairs(str[1:]))
print(countPairs('hihih'))

#countABC:
def countABC(str):
	if len(str) < 3:
		return 0
	if str[0] == 'a' and str[1] == 'b' and str[2]== 'c':
		return (1 + countABC(str[1:]))
	elif str[0] == 'a' and str[1] == 'b' and str[2]== 'a':
		return (1 + countABC(str[1:]))	
	else: 
		return (0 + countABC(str[1:]))
print(countABC('abaxxaba'))

#count11: work for most but fails in this test
def count11(str):
	if len(str) < 2:
		return 0
	if (len(str) > 2 and str[0] == '1' and str[1] == '1' and str[2] != '1') :
		return (1 + count11(str[1:]))
	if len(str) == 2 and str[0] == '1' and str[1] == '1':
		return (1 + count11(str[1:]))
	else:
		return (0 + count11(str[1:]))
print(count11('11x111x1111'))

#stringClean
def stringClean(str):
	if len(str)<2:
		return str
	if str[0] == str[1]:
		return stringClean(str[1:])
	else:
		return str[0] + stringClean(str[1:])
print(stringClean('abbcdd'))
		
#countHi2
def countHi2(str):
	if len(str) < 2:
		 return 0
	if str[len(str)-2:len(str)] == "hi":
		if len(str) > 2 and str[len(str)-3] != 'x' or len(str) == 2:
			return 1 + countHi2(str[len(str)-1:])
	return countHi2(str[len(str)-1:])
print(countHi2("xhixhi"))


#parenBit
def parenBit(str):
	if str == '':
		return str
	if str[0] == '(':
		if str[len(str)-1] == ')':
			return str
		else:
			return parenBit(str[:len(str)-1])
	else:
		return (parenBit(str[1:]))
print(parenBit('x(hello)'))

#nestParen
def nestParen(str):
	if str == "":
		return True
	if str[0] == '(' and str[len(str)-1] == ')':
		return nestParen(str[1 : len(str)-1])
	else:
		return False
print(nestParen("(())"))


#strCount
def strCount(str, sub):
	if len(str) < len(sub):
		return 0
	if str[:len(sub)] == sub:
		return (1 + strCount(str[len(sub):], sub))
	return strCount(str[1:], sub)
print(strCount('catcowcat', 'cow'))

#strCopies: no idea except unless use the previous
def strCopies(str, sub, n):
	if len(str) < len(sub):
		return False
	c = strCount(str, sub)
	if c == n:
		return True
	else: 
		return False
print(strCopies('catcowcat', 'cat', 2))		

#strDist: Give up...
	
	