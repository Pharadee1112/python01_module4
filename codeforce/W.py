all_number = int(input())

tatal_number = all_number * (all_number + 1) // 2
count = 0  


for member in range(all_number - 1) :
    member = int(input())
    count += member

if count != tatal_number :
    print(tatal_number - count)


# print(tatal_number)
# print(count)