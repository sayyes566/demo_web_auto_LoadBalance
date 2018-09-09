from threading import Timer

def timeout():
    print("Game over")

# duration is in seconds
t = Timer(5, timeout)
t.start()

# wait for time completion
t.join()
