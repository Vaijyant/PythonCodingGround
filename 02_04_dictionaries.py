dict_obj = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(dict_obj)

print(dict_obj["model"])
print(dict_obj.get("model"))

dict_obj["year"] = 2018
print(dict_obj)

print("Iteration (via keys):")
for x in dict_obj:
    print("\t", dict_obj[x])

print("Iteration (via values):")
for x in dict_obj.values():
    print("\t", x)


print("Iteration (via key, values):")
for x, y in dict_obj.items():
    print("\t", x, y)


print(len(dict_obj))

dict_obj["color"] = "red"
print(dict_obj)

del dict_obj["model"]
print(dict_obj)

print(dict_obj.pop("color"))
print(dict_obj)

print(dict_obj.popitem())
print(dict_obj)
