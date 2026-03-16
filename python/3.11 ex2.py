# yaz
import operations #import the module with functions

def main():
    print("Simple Modular Calculator")
    a= float(input("Enter first number:"))
    b= float(input("Enter second number:"))
    op= input("Enter operation (+,-,*,/):")

    if op== '+':
        result= operations.add(a,b)
    elif op == '-':
        result== operations.substract(a,b)
    elif op == '*':
        result = operations.multiply(a,b)
    elif op == '/':
       try:
        result: operations.divide(a,b)
      except ValueError as e:
        print(e)
        return
    else:
        print("Invalid Operation!")
        return
    print(f"Result: {result}")

if __name__ = "__main__":
main()

#son iki satitin ne ise yaradigini bulmak odev
