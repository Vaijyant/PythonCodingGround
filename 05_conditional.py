a = 33
b = 200
if b > a:
    print("b is greater than a")
elif b == a:
    print("a and b are equal")
else:
    print("a is greater than b")


# shorthand
print("A") if a > b else print("B")

## 
input1 = input("Please enter a test string: ")

if len(input1) < 6:
    print("Your string is too short.")
    print("Please enter a string with at least 6 characters.")


input2 = input("Please enter a number: ")
input2 = int(input2)

if input2%2 == 0:
    print("Even")
else:
    print("Odd")