set_obj = {"apple", "banana", "cherry"}
print(set_obj)

print("Iteration:")
for x in set_obj:
    print("\t", x)

set_obj.add("orange")
print(set_obj)

set_obj.update(["orange", "mango", "grapes"])
print(set_obj)

print(len(set_obj))

set_obj.remove("orange")
print(set_obj)

set_obj.discard("banana")
print(set_obj)

el_pop = set_obj.pop()
print(el_pop)
print(set_obj)