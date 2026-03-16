#funstion that returns the minimum and maximum values of the given array

def find_min_max(arr):
    return min(arr), max(arr)
arr= [3,1,17,9,2]
print(find_min_max(arr))  #output: (1,17)