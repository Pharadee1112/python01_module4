word = input()

word_len = len(word)

for character in range(word_len // 2) :
    if word[character] != word[word_len - 1 - character] :
        print("NO")
        exit()

print("YES")