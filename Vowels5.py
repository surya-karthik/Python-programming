#Program to print vowels using intersection method in sets..
#intersection method in sets ,takes the objects in one set and compares them to those in another, then reports on any common objects found. 


vowels = {'a','e','i','o','u'}
#vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")

             
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)
    

