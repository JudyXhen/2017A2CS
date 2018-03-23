Task 1.1
It is applied in the designing stage and helps us to be clear on the structure of the program.


Task 1.2
The star symbol means repetition, which is to keep inputting values for different variables. 
The circle at right corner means selection, which represent Boolean variables.

Task 1.3
 WHILE NOT EOF(SaleryFile)
  CALL ReadSalary
  IF Salary>50:
   THEN
    IF Salary >=90:
     THEN 
      Role <- ‘Project manager’
     ELSE:
      Role <- ‘Lead developer’
    ENDIF
   ELSE:
    Role <- ‘Assign manager’
  ENDIF
 ENDWHILE


Task 1.4
see the file Task1-4-diagram.jpeg


 
Task 1.5
 WHILE Finished == FALSE:
  CALL ReadSalary
  IF Salary>50:
   THEN
    IF Salary >=90:
     THEN 
      Role <- ‘Project manager’
     ELSE:
      Role <- ‘Lead developer’
    ENDIF
   ELSE:
    IF Salary > 70:
     THEN
      Role <- ‘Consultant’
     ELSE:
      Role <- ‘Assign manager’
    ENDIF
  ENDIF
 ENDWHILE

Task 1.6
def IdentifyRole(Salary):
 while finished == false:
  ReadSalary()
  if Salary>50:
   if Salary >=90:
    Role <- ‘Project manager’
   else:
    Role <- ‘Lead developer’
  elif Salary > 70:
   Role <- ‘Consultant’
  else:
   Role <- ‘Assignment manager’
 return Role