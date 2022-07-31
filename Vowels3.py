#Program to print vowels from a given word and also print its frequency(count)
#To count vowels frequency in this code we used an empty dictionary... 


vowels = ['a','e','i','o','u']
word = input("Provide a word to search for Vowels: ")

found = {}   #Create an empty dictionary.



# First We’ve initialized all the vowel counts to 0. 

found ['a'] = 0
found ['e'] = 0
found ['i'] = 0
found ['o'] = 0
found ['u'] = 0


for letter in word:
    if letter in vowels:
        found[letter] +=1   #Increment the value referred to by “found[letter]” by one

#As the “for” loop is using the “items” method, we need to provide two loop variables, “k” for the key and “v” for the values.
#items method, will returns a list of the key/value pairs. A buit-in method in dictionaries.
#sorted built-in function is used to sort the vowels in an alphabetical order. ecause dictionaries stores the key value pairs in an UNORDERD way

        
for k, V in sorted(found.items()):
    print(k, "was found" ,V, "time(s).")
