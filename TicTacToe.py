import random

one = str(1)
two = str(2)
three = str(3)
four = str(4)
five = str(5)
six = str(6)
seven = str(7)
eight = str(8)
nine = str(9)
move = 0

positions = [1,2,3,4,5,6,7,8,9]

def BoardStatus():
	print(" " + one + " | " + two + " | " + three + " \n---|---|---\n " + four + " | " + five + " | " + six + " \n---|---|---\n " + seven + " | " + eight + " | " + nine + " ")

def PlayerAction():
	move = int(input("Enter the number of the place you want the X to appear: "))
	return(move)
	
def MoveMap(move):
	if move == 1:
		one = str("X")
	elif move == 2:
		two = str("X")
	elif move == 3:
		three = str("X")
	elif move == 4:
		four = str("X")
	elif move == 5:
		five = str("X")
	elif move == 6:
		six = str("X")
	elif move == 7:
		seven = str("X")
	elif move == 8:
		eight = str("X")
	elif move == 9:
		nine = str("X")
	return("x")

BoardStatus()
PlayerAction()
MoveMap(move)

BoardStatus()
#print(" " + one + " | " + two + " | " + three + " \n---|---|---\n " + four + " | " + five + " | " + six + " \n---|---|---\n " + seven + " | " + eight + " | " + nine + " ")