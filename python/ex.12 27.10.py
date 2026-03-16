#ex.12
# takes an array as input and returns a new array with elements in reverse order

def reverse_array(arr):
    return arr[:: -1]
arr = [1,2,3,4,5]
print(reverse_array(arr)) #output: [5,4,3,2,1]