a = " Hello World! "
print(a[1]) # indexing from 0

# substring
print(a[2:7]) # prints [2, 7)

# removing leading and trailing white space characters
print(a.strip()) # this does not modify the a itself, returns a modified string
print(a)

# lenght of the string
print(len(a))

# to lower and upper case
print(a.lower())
print(a.upper())
print(a) # upper() and lower() return a new string

# replace a string
print(a.replace("World", "Vaijyant"))
print(a) # replace() returns a new string

# split
print(a.split(" "))
