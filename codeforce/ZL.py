all_number = int(input())
element = input().split()

only = []

for index in element:
    if index not in only :
        only.append(index)

print(len(only))