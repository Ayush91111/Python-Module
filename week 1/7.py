text = input("Enter sentence: ")
words = text.split()
for i in range(len(words)):
  if i % 2 == 1:
        word = words[i]
        words[i] = word[::-1]

print(" ".join(words))