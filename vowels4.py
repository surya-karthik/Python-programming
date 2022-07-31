vowels = ['a','e','i','o','u']
word = input("Provide a word to search for Vowels: ")

found = {}




for letter in word:
    if letter in vowels:
        found.setdefault(letter,0)
        found[letter] +=1



        
        
for k, V in sorted(found.items()):
    print(k, "was found" ,V, "time(s).")

    
    
   
# We used setdefault method to initialize a nonexistent key to a supplied default value.“setdefault” is also used to  avoid the “KeyError” exception.
#The setdefault method does what the two lines if/ not in statements do, by using a single line of code.

                                     
