#a simple stack using a list
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Top element:", stack[-1]) #shows the element added 30

removed = stack.pop()
print("Removed element:", removed)
print("Stack after pop:", stack)