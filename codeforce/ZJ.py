all_number = int(input())
element_list = input().split()

for character in element_list[::2]:
    print(character, end=" ")