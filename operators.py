# Arithmetic Operators
x = 2
y = 5
print("Arithmetic Operators")
print("x + y: " + str(x + y))
print("x - y: " + str(x - y))
print("x * y: " + str(x * y))
print("x / y: " + str(x / y))
print("x % y: " + str(x % y))
print("x ** y: " + str(x ** y))
print("x // y: " + str(x // y))

# Comparision operators
print("\nComparision Operators")
print("x == y: " + str(x == y))
print("x != y: " + str(x != y))
print("x > y: " + str(x > y))
print("x < y: " + str(x < y))
print("x >= y: " + str(x >= y))
print("x <= y: " + str(x <= y))

# Logical operators
print("\nLogical Operators")
a = True
b = False
c = True
print(a and b)
print(a or b)
print(not b)

z = 2
# Identity operators
print("\nIdentity Operators")
print("z is x:", a is x)
print("a is c:", a is c)
print("y is not x:", y is not x)
print("y is not b:", y is not b)

# Membership operators
print("\nMembership Operators")
x = ["apple", "banana"]
print("banana" in x)
print("pineapple" not in x)

# Bitwise operators
print("\nBitwise Operators")
bits_1 = 0b10101
bits_2 = 0b01111
print("bits_1 & bits_2:", bin(bits_1 & bits_2))
print("bits_1 | bits_2:", bin(bits_1 | bits_2))
print("bits_1 ^ bits_2:", bin(bits_1 ^ bits_2))
print("~bits_1:", bin(~bits_1))
print("bits_1 << 2:", bin(bits_1 << 2))
print("bits_2 >> 2:", bin(bits_2 >> 2))

