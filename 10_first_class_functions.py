def square(x):
    return x ** 2

f = square(5)
print(square)
print(f)

print("=======")

ff = square
print(square)
print(ff)

print(ff(5))

print("=======")

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])

print(squares)

def cube(x):
    return x ** 3

cubes = my_map(cube, [1, 2, 3, 4, 5])
print(cubes)

print("=======")

def logger(msg):
    def log_message():
        print('Log:', msg)
    return log_message

log_hi = logger('Hi')
log_hi()

print("=======")

def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text


print_h1 =  html_tag('h1')
print(print_h1)
print_h1('Test Headline!')
print_h1('Another Headline!')