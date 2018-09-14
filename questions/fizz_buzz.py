for i in range(16):
    ans = ""
    
    if i%3 == 0:
        ans = ans + "Fizz"
    if i%5 == 0:
        ans = ans + "Buzz"
    
    if not ans:
        print(i)
    else:
        print(ans)