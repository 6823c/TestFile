import threading

def Sum(low, high):
    total = 0;
    for i in range(low, high):
        total += i
    print("SubThread :", total)

t = threading.Thread(target=Sum, args=(1, 100000))
t.start()

print("Main Thread")