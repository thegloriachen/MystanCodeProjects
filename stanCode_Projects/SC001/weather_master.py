"""
File: weather_master.py
Name: Gloria
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program should implement a console program that asks weather data from user to compute the
	average, highest, lowest, cold days among the inputs.
	"""
	print("stanCode \"Weather Master 4.0\"!")
	data = int(input("Next Temperature: (or " + str(EXIT) + " to quit)? "))
	#判斷邊界條件
	if data == EXIT:
		print("No temperatures were entered.")
	else:
		maximum = data
		minimum = data
		average = data
		count = 0
		count_cold_days = 0
		#first input
		count +=1
		if data < 16:
			count_cold_days +=1
		#while loop
		while True:
			data = int(input("Next Temperature: (or " + str(EXIT) + " to quit)? "))
			#判斷邊界條件
			if data == EXIT:
				break
			#find maximum
			if data > maximum:
				maximum = data
			#find minimum
			if data < minimum:
				minimum = data
			#find cold days
			if data < 16:
				count_cold_days +=1
			#sum total temperatures
			average += data
			#count inputs
			count += 1
		print("Highest temperature = " + str(maximum))
		print("Lowest temperature = " + str(minimum))
		print("Average = " + str(average / count))
		print(str(count_cold_days) + " cold day(s)")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
