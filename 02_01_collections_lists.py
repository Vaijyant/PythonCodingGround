# Four collection types in Python
# 1) List
# 2) Tuple
# 3) Set
# 4) Dictionary

list = ["James", "Harry", "Albus"]
print("List:", list)

print("List item at 2:", list[2])

list[0] = "Percevel"
print("List:", list)

print("Iteration:")
for x in list:
    print("\t", x)

print("List length:", len(list))

list.append("Ginny")
print("List:", list)

list.insert(1, "James")
print("List:", list)

list.remove("Percevel")
print("List:", list)

print(list.pop())
print(list)

del list[2]
print(list)

list.clear()
print(list)
