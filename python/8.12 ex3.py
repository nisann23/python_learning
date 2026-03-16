#simulate a bank queue ...

from collections import deque
customers = deque([
    ("Patricia", 5),
    ("Bob", 3),
    ("francisca", 7),
    ("Diana",2)
])

total_waiting_time= 0
current_time = 0

while customers:
    name,time = customers.popleft()
    print(f"Serving {name}, waited {current_time} minutes")
    total_waiting_time += current_time
    current_time += time

    print("Total waiting time:", total_waiting_time)