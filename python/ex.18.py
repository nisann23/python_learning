#a funtion that increases all prices by 5 percent in the array
def adjust_for_inflation(prices, inflation_rate):
    return [round(price *(1 + inflation_rate/100), 2) for price in prices]

prices= [100,200,300,400]
inflation_rate = 5 #%5 increase
print(adjust_for_inflation(prices, inflation_rate))  