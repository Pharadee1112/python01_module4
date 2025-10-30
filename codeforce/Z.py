word = str(input())
insert = str(input())

count = (len(word) // 2)
print(word[:count] + insert + word[count:])