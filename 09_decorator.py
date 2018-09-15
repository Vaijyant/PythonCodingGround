
def check(checking_divide):
    def check_divide(a, b):
        if b == 0:
            print("Can't divide by zero.")
            return
        checking_divide(a, b)
    return check_divide

@check
def divide(a, b):
    return a/b

print(divide(5, 0))