import random

for i in range(10):
    print(random.random()) # Uniform distribution

def my_random():
    return 4*random.random() + 3

print("=======")
for i in range(10):
    print(my_random())


print("=======")
for i in range(10):
    print(random.uniform(3, 7))


print("=======")
for i in range(20):
    print(random.normalvariate(0, 5))

print("=======")
for i in range(20):
    print(random.randint(1, 6))

print("=======")
outcomes = ['rock', 'paper', 'scissors']

for i in range(20):
    print(random.choice(outcomes))