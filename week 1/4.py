name = input("Enter your name: ")
space = name.index(" ")
first = name[0]
last = name[space + 1]
print("Your initials are:", first.upper() + "." + last.upper())