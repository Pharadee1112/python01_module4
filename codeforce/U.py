first_number = int(input())
second_number = int(input())

# if first_number % 2 == 0 :
#     first_number += 0

if first_number % 2 != 0 :
    first_number += 1  

for i in range(first_number, second_number + 1, 2):
    print(i)

