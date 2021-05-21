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

print(" " + one + " | " + two + " | " + three + " \n---|---|---\n " + four + " | " + five + " | " + six + " \n---|---|---\n " + seven + " | " + eight + " | " + nine + " ")

move = int(input("Enter the number of the place you want the X to appear: "))

if move == 1:
	one = str("X")
elif move == 2:
	two = str("X")

print(" " + one + " | " + two + " | " + three + " \n---|---|---\n " + four + " | " + five + " | " + six + " \n---|---|---\n " + seven + " | " + eight + " | " + nine + " ")