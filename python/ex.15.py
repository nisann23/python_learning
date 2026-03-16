# function that returns the second largest element in the given array
def second_largest(arr):
    unique_elements = list(set(arr)) #remove duplicates
    if len(unique_elements) <2:
        return None  #no second largest element
    unique_elements.sort()
    return unique_elements[-2]
arr = [4,2,7,7,1]
print(second_largest(arr))