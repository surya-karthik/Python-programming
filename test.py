#Using Intersection method in Sets {}

vowels = {'a','e','i','o','u'}
word = input("type your word: ")


#intersection method in sets ,takes the objects in one set and compares them to those in another, then reports on any common objects found. 


r = vowels.intersection(set(word))
print(r)
