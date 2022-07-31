# Program to print vowels by taking vowels from user input  into an empty list!

vowels = ['a', 'e','i','0','u']
word = input("Provide a word to search for Vowels: ")
found = []
for letter in word:
	if letter in vowels:
			if letter not in found:
				found.append(letter)
						
for vowel in found:
	print(vowel)
		
