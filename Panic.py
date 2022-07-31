#Program to transform the string "Don’t panic!" into the string "on tap" using only the list methods.


phrase = "Don't Panic!"

Plist = list (phrase)

print (phrase)
print(Plist)

#The below loop pops the last four objects from “plist”. No more “nic!”

for i in range(4):  
 Plist.pop()
 
Plist.pop(0)   #Get rid of the ‘D’ at the starting index of the list.


Plist.remove("'")


# Swap the two objects at the end of the list by first popping each object from the list, then using the popped objects to extend the list.
#( the pops opereration occur *first* in the order shown, then the extend happens.)


Plist.extend([Plist.pop(), Plist.pop()])  

#The below line of code pops the space from the list, then inserts it back into the list at index location 2.
#(Just like the above line of code, the pop occurs *first*, before the insert happens. And, remember: spaces are also characters, too in python.)


Plist.insert(2, Plist.pop(3))



new_phrase = ''.join(Plist)
print(Plist)
print(new_phrase)

