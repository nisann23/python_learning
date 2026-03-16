#ex2
#Economic data for the employee
gross_salary= 3500.75 #gross salary(float)
tax_rate=0.10 #income tax rate 10%(float)
pension_contrib= 0.05 #pension contribution 5% (float)

#calculate taxes and contributions
income_tax = gross_salary * tax_rate #float
pension_contribution = gross_salary * pension_contrib #float

#calculate net salary
net_salary= gross_salary - (income_tax + pension_contribution)

#display results
print(f"Gross Salary: {gross_salary} lei")  #f olunca arasindaki seyleri okuyormus
print(f"Income Tax: {income_tax} lei")  #R daki cat gibi sanirim
print(f"Pension Contribution: {pension_contribution} lei")
print(f"Net Salary: {net_salary: .2f} lei")  # .2f olmasinin sebebi virgulden sonra 2 sayi olmasi icin