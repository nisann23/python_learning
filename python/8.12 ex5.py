from collections import deque

queue = deque()

def add_customer(name, priority= False):
    if priority:
        queue.appendleft(name)
    else:
        queue.append(name)

def serve_customer():
    if queue:
        print ("Serving", queue.popleft())
    else:
        print("No customers.")

add_customer("Regular1")
add_customer("VIP1", priority= True)
add_customer("Regular")
serve_customer()
serve_customer()
serve_customer()