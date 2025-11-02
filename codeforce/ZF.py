word = input()

word_len = len(word)

for character in range(word_len // 2) :
    if word[character] != word[word_len - 1 - character]:
    # print(word[character])
        # print(word[word_len - 1 - character])


# p = "kam"
# d = len(p)
# f = d // 2
# print(p[d - 1 - f])