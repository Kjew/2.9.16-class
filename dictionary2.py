vocabulary_words = {"bear":"Big animal, lives in woods. Grrrrr", "tiger":"Big cat, lives in jungle, orange fur, stripes, grrrrr.", "lions": "Big cat, lives in plains, rarrrrrrrrr", "owl":"Birdie, lives in a barn or a tree, you know. Hoo Hoo."}

def letter_count(name):
	print "Name:", name
	count = {}
	for letter in name:
		if letter not in count:
			count[letter] = 1
		else:
			count[letter] += 1
	return count


name = raw_input("Enter your name:")
print letter_count(name)

prices = { "banana": 4, "apple": 2, "orange": 1.5, "pear": 3 }

def most_expensive():
	for fruit, price in prices.values():
		if price 
