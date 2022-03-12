## If my dict = {'a':15 , 'c':35, 'b':10}, write Python code:
##a. to print all the keys.
##b. to print all the values.
##c. to print all the keys and values pairs.
##d. to print all the keys and values pairs in order of key.
##e. to print all the keys and values pairs in order of value.
d = {'a': 15, 'c' : 35, 'b' : 10}
keys = list(d.keys())
keys.sort()
values = list(d.values())
print("Keys: ", keys)
print("Values: ", values)
print("Key-value pairs")
for i,j in d.items():
    print(i,j)
print("Key-value pairs- sorted by key")
for i,j in sorted(d.items()):    
    print(i,j)
values = d.values()
print("Key-value pairs- sorted by value")
for i in sorted(d.values()):
    print(list(d.keys())[list(d.values()).index(i)],i)

    
