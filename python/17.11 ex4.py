import csv

companies_data = [
    ["Company", "Revenue(in millions)"],
    ["Apple", "394"],
    ["Microsoft", "198"],
    ["Amazon", "469"],
    ["Google", "280"],   
    ["Tesla", "81"]
]

with open("companies.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(companies_data)

print("The file companies.csv has been created")

def find_max_revenue(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        
        # ÖNEMLİ: Başlık satırını (ilk satırı) atla
        next(reader) 
        
        # row{1} yerine row[1] yapıldı
        revenues = [int(row[1]) for row in reader] 
        
        return max(revenues)
     
max_revenue = find_max_revenue("companies.csv")
print(f"The highest revenue is: {max_revenue} million dollars")