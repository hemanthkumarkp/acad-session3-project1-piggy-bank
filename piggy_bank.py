def depositMoney(money):
    global totalMoney
    totalMoney = totalMoney+int(money)

def withdrawMoney(money):
    global totalMoney
    totalMoney = totalMoney-int(money)  

def checkBalance():
    global totalMoney
    return (totalMoney)

def calculateInterest():
    numberOfYears = input("Number of years for interest : ")
    global totalMoney
    return ((totalMoney*12*(int(numberOfYears)))/100)

totalMoney=0
start = input("start or end : ")

while(start=='start'):
	op = input("deposit or withdraw or check or interest : ")
	if(op=='deposit'):
		amt = input("enter deposit amount : ")
		depositMoney(amt)
		print('After deposit balance is :',checkBalance())
		start = input("start or end : ")
	elif(op=='withdraw'):
		amt = input("enter withdraw amout : ")
		withdrawMoney(amt)
		print('after withdraw balance is :',checkBalance())
		start = input("start or end : ")
	elif (op=='check'):
		print('account balance is : ',checkBalance())
		start = input("start or end : ")
	elif (op=='interest'):
		intrAmt = calculateInterest()
		print('interest amount is :',intrAmt)
		totalMoney = totalMoney + intrAmt
		start = input("start or end : ")
	else:
		print("wrong option, try again : ")
		start = input("start or end : ")
else:
	print(" exiting program ")

        
