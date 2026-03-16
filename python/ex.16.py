#function that takes a list of monthly revenues and returns the avarage revenue
def average_revenue(revenues):
    return sum(revenues)/ len(revenues) if revenues else 0  #if revenues bos degilse calistir anlamina geliyor
revenues = [5000, 7000, 6500, 8000, 7200]
print(average_revenue(revenues)) 