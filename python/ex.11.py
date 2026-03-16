#function that extracts the company name from an email adress
def extract_company(email):
    #split the email at @ to seperate the username from the domain
    #then, split the domain at '.' to get the company name
 return email.split("@")[1].split(".")[0]
print(extract_company("andreea.bogoslov@ulbsibiu.ro"))
print(extract_company("alice.smith@bankingworld.org"))

