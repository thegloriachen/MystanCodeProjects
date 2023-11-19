"""
File: prime_checker.py
Name: Gloria
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""


# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program asks our user for input and checks if the input is a prime number or not.
	"""
	print("Welcome to the prime checker!")
	data = int(input("n: "))
	#判斷邊界條件
	if data == EXIT:
		print("Have a good one!")
	else:
		#for first input
		number = data - 1
		#判斷邊界條件
		if data == EXIT:
			print("Have a good one!")
		else:
			if number == 1:
				print(str(data) + " is a prime number.")
			else:
				#while loop
				while True:
					if number == 1:
						print(str(data) + " is a prime number.")
						break
					if data % number == 0:
						print(str(data) + " is not a prime number.")
						break
					if data % number != 0:
						number = number - 1
		#for next input
		#while loop
		while True:
			data = int(input("n: "))
			number = data - 1
			#判斷邊界條件
			if data == EXIT:
				print("Have a good one!")
				break
			if number == 1:
				print(str(data) + " is a prime number.")
			else:
				#while loop
				while True:
					if number == 1:
						print(str(data) + " is a prime number.")
						break
					if data % number == 0:
						print(str(data) + " is not a prime number.")
						break
					if data % number != 0:
						number = number - 1


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
