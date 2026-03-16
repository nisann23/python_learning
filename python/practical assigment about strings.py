# 1. Create a Hypothetical Dataset
date = "10-11-2024"
customer_name = "Nisa Unal"
product = "shoes"
comment = "It is comfartable.I like the quality and I like the color."
transactionID = "1222689874 TR-34"

# 2. Perform String Manipulation

# Extract and print the first name of the customer
first_name = customer_name.split()[0]
print(first_name)

# Convert the customer review to lowercase for standardization
comment_lower = comment.lower()
print(comment_lower)

# Count how many times a certain keyword appears in the review
keywords_to_count = ["like"] # Sadece 'like' kelimesini saymak daha nettir
total_mentions = 0

for keyword in keywords_to_count:
    count = comment_lower.count(keyword)
    total_mentions += count
    
# Not: "I" kelimesini tam kelime olarak saymak isterseniz daha karmaşık yöntem gerekir.
# Basitlik için sadece "like" kelimesi ve toplam sayısını yazdıralım.
print(f"'{keywords_to_count[0]}' kelimesi {total_mentions} kez geçti.")


# Extract and print only the numeric part of the Transaction ID
numeric_part = ""
for char in transactionID:
    if char.isdigit():
        numeric_part += char

print(numeric_part)

