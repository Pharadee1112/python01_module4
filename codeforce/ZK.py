all_number = int(input())
element = input().split()
# print(type(element))

for index in element:
    if int(index) % 2 == 0:
        print(index, end=" ")