#ex4
#taking inputs from the user
revenue= float(input("enter the total revenue of the business:"))
expenses= float(input("enter the total expenses of the business:"))
tax_rate= float(input("enter the tax rate (as a percentage):"))

#calculating profit
profit = revenue - expenses

#calculating tax paid (tax_rate is a percentage)
tax_paid= (tax_rate /100)*revenue

#calculating profit margin(percentage)
profit_margin = (profit / revenue) *100

#displaying results
print(f"\nResults:")
print(f"total revenue: {revenue} USD")
print(f"total expences: {expenses} USD")
print(f"profit: {profit} USD")
print(f"tax paid: {tax_paid} USD")
print(f"profit margin: {profit_margin: .2f}%")