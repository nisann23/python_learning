#exercise 6
#asking the user how many days of sales they want to track
days= int(input("How many days so you want to track the sales for?"))

#initializing a variable to store total revenue
total_revenue= 0

#loop to collect sales data for each day
for day in range (1, days+1):
    daily_sales = float(input(f"Enter the sales amount for day {day}:"))
    total_revenue += daily_sales  #adding the daily sales to the total revenue

#printing the total revenue after the loop
print(f"\n Total revenue after {days} days: {total_revenue} USD")