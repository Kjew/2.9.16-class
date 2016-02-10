#Write a function that returns True if it's prime or False if it's not prime
#Ask the user to enter an integer to check if it's prime. If prime print that it's prime, otherwise print that it's not. 
#A prime number is a whole number greater than 1 that is only divisible by 1 and itself (2,3,5,7,11)

def is_prime(num):
	for i in range(2,num): #start counting at 2, count up to num 
		if (num % i == 0): #2,3,4, 5 etc up to num 
			return False
	return True

user_input = int(raw_input("give me a #: "))
if is_prime(user_input) is True:
	print "%i is prime!" % (user_input)
else: print "%i is not prime" % (user_input)

