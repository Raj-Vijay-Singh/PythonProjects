email = input("Enter your email: ")
start = email.find("@")
domain = email[start+1:]
print(domain)