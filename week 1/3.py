email = input("Enter your email address: ")
at_position = email.index("@")
domain = email[at_position + 1:]
print("Domain:", domain)