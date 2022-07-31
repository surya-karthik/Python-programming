paranoid_android = "Marvin, the Paranoid Android"

letters = list(paranoid_android)

#The first loop iterates over a slice of the first six objects in the list.

for char in letters[:6]:
    print('\t', char)
print()


#The second loop iterates over a slice of the last seven objects in the list. Here “*2” inserts two tab characters before each printed object.

for char in letters[-7:]:
    print('\t'*2,char)
print()


#The third loop iterates over a slice  from within the list, selecting the characters that spell the word “Paranoid” in the list.
#Here “*3” inserts three tab characters before each printed object.

 for char in letters[12:20]:
    print('\t'*3, char)
