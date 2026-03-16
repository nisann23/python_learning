#ex3
#taking the two integer inputs from the user
num1= int(input("Enter the first integer:"))
num2= int(input("Enter the second integer"))

#calculating the sum, difference, product and quotient
sum_result = num1+num2
difference_result = num1-num2
product_result= num1*num2
quotient_result = num1/num2 if num2 !=0 else "undefined" #check for division by zero

#printing the results
print(f"sum: {sum_result}")
print(f"difference: {difference_result}")
print(f"product: {product_result}")
print(f"quotient: {quotient_result}")

#comparing the two numbers

if num1 == num2:
    print("the two numbers are equal")
elif num1>num2:
    print("the first number is greater than the second")
else:
    print("the first number is lesser than the second")