import csv

data = [
    ["Name", "Age"],
    ["John", 30],
    ["Maya", 25],
    ["Robert", 35],
    ["Maria", 40]
]

# Dosyayı yazma modunda aç
with open("people.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file 'people.csv' created successfully!")