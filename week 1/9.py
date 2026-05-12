word = input("Enter a word: ")
if len(word) > 1:
  new_word = word[-1] + word[1:-1] + word[0]
else:
 new_word = word
print("New word:", new_word)