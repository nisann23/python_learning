#function that rotates an array called arr to the rigth by k
def rotate_array(arr, k):
    k= k % len(arr)  #handle cases where k>len(arr)
    return arr[-k:] + arr[:-k]
arr= [1,2,3,4,5]
print(rotate_array(arr,2)) #outut: [4,5,1,2,3]
#k bolu len yapiyoruz k degeri 2 yani 5 bolu 2 oluyor o da 2 oldugu icin 2. den baslayip gidiyor