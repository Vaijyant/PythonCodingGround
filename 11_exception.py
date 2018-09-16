# f = open('11test.txt') # error line

try:
    f = open('11_test.txt')
    var = bad_var
except FileNotFoundError:
    print('Sorry. This file does not exists.')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing the finally block")


print("======================")

try:
    f = open('11_test.txt')
    if f.name == '11_test.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print("Executing the finally block")
