# queues and stacks
#simple queue using a list
queue = []

queue.append("A")
queue.append("B")
queue.append("C")

print("First in line:", queue[0])

first = queue.pop(0)
print("Removed from queue:", first)
print("Queue after dequeue:", queue)
