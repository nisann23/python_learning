#function that shows the max of which month
def max_revenue_month(revenues, months):` #def fonk tanimlamak icin kullanilir`
    max_index = revenues.index(max(revenues))
    return months[max_index]
revenues = [5000, 7000, 6500, 8000, 7200]
months= ["Jan", "Feb", "Mar", "Apr", "May"]
print(max_revenue_month(revenues, months))