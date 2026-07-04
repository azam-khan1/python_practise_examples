import threading
import time

def take_order():
    for i in range (1,4):
        print(f"taking order for id no:{i} ")
        time.sleep(2)


def brew_chai():
    for i in range (1,4):
        print(f"brewing chai for id no:{i}")
        time.sleep(3)

#now creating threads 
order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

# after both threads ends they will be giving this output 
order_thread.join()
brew_thread.join()

print(f"all students have taken their tea.")