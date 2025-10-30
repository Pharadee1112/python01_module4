word = str(input())
new_word = len(word) // 2
print(word[new_word:] + word[:new_word])