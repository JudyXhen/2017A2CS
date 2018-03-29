#Judith Chen S3C5

——————————————————
Task 28.01
-
LDM #2
STO A
-
LDM #10
STO B
-
LDD A
ADD B
STO C
-
LDD B
XOR #&FF
INC ACC
STO B
LDD A
ADD B
STO D



———————————————————
Task 28.02
-
	LDD A
	CMP 0
	JPN THEN
	JPE ELSE
THEN:	LDD A
	STO B
ELSE:	LDD B
	DEC ACC
	STO B 





———————————————————
Task 28.03
-
	LDM #1 
	STO Number
	LDM #0
	STO Total
	LDM #5
	STO Max

LOOP:	LDD Total
	ADD Number
	STO Total
	LDD Number
	INC ACC
	STO Number
UNTIL:	CMP Max
	JPN LOOP
ENDLOOP:


———————————————————
Task 28.04
-
	LDM #0
	STO Count
LOOP:	LDD Count
	INC ACC
	IN 
	STO Character
	CMP #78
	JPN LOOP




———————————————————
Task 28.05
-
	LDM #0
	STO Count
LOOP:	LDD Count
	INC ACC
	STO Count
	IN 
	STO Character
	CMP #78
	JPN LOOP
	JPE OUTPUT
OUTPUT:	LDD B
	OUT
	CMP #13
	JPN OUTPUT
	END



———————————————————
TASK 28.06 
Can’t access memory.
the differences from the previous is to Count the length of the word and decrease the value of count by one each time, store each character and present that stored element.  
