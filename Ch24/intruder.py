#Judith S3C5 

#-------------------------------------------
#InitialStates
SysActive = False
AlarmBellRings = False
AlertMode = False

#Lets Print These lol
SysInactiveOutput = 'System Inactive'
SysActiveOutput = 'System Active'
BellRingsOutput = 'Alarm Bell Rings'
AlertModeOutput = 'Alert Mode'

#MENU for users
def Menu():
	Choice = int(input('What do you want to do? 1-Press Button, 2-Enter PIN, 3-Wait for two minutes, 4-Activate Sensor\n'))
	print('\n')
	if Choice == 1:
		PressButton(SysActive)
	elif Choice == 2:
		EnterPIN(SysActive, AlertMode, AlarmBellRings)
	elif Choice == 3:
		TwoMinsPass(AlertMode, AlarmBellRings)
	elif Choice == 4:
		ActivateSensor(SysActive, AlertMode)
	else: 
		print("Wrong imput. Enter again.")
		Menu()
		

#The Actions
def PressButton(SysActive): 
	if SysActive == False:
		SysActive = True
	print(SysActiveOutput)
	return SysActive

def EnterPIN(SysActive, AlertMode, AlarmBellRings):
	if SysActive == True:
		SysActive = False
	if AlertMode == True: 
		SysActive = False
		AlertMode = False
	if AlarmBellRings == True:
		SysActive = False
		AlarmBellRings = False
	print(SysInactiveOutput)
	return SysActive, AlertMode, AlarmBellRings
	
def TwoMinsPass(AlertMode, AlarmBellRings):
	if AlertMode == True:
		AlertMode = False
		AlarmBellRings = True
	print('Two minutes passed.')
	print(BellRingsOutput)
	return AlertMode, AlarmBellRings
	
def ActivateSensor(SysActive, AlertMode):
	if SysActive == True:
		SysActive = False
		AlertMode = True
	print(AlertModeOutput)
	return SysActive, AlertMode
	
Menu()
	


