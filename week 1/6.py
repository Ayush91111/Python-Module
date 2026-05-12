password = input("Enter your password: ")

letter = any(char.isalpha() for char in password)
number = any(char.isdigit() for char in password)
special = any(char in "@#$&" for char in password)

if len(password) < 6 or password.isalpha():
    print("Weak Password")
elif len(password) >= 8 and letter and number and special:
    print("Strong Password")
elif len(password) >= 6 and letter and number:
    print("Moderate Password")
else:
    print("Weak Password")