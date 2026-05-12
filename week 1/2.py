numbers = [12, 15, 22, 35, 48, 55, 60, 10]
for num in numbers:
    if num > 50:
        print("Number greater than 50 encountered. Stopping loop.")
        break
    if num % 5 == 0:
        continue

print(num)