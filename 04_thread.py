import threading

def loop():
    for i in range(1, 11):
        print(i)

def loop2():
    for i in range(21, 31):
        print(i)

threading.Thread(target=loop).start()
threading.Thread(target=loop2).start()