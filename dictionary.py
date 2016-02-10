vocabulary_words = {"contatenation":"adds values together", "integer": "whole number", "float" : "number with decimals", "functions": "reusable formula to repeat code"}



def name_count(name):
	#name = name.upper()
	letter_count = {} #creating a dictionary w key value pairs letter:# times appears
	for letter in name.upper: #for each letter in name (eg. iterating through each letter in name)
		if letter in letter_count is True: #checking if the key letter is in the dictionary letter_count
			number = letter_count[letter] #accessing the dicitonary w the key letter, storing in variable number
			letter_count[letter] = number + 1 #update values by 1
		else: letter_count[letter] = 1 #make new key value pair

name = raw_input("Tell me your name!")
print name_count(name)