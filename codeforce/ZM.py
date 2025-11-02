number = int(input())
element = input().split()


for index in range(number):
    element[index] = int(element[index])
    print(element[index])

for i in range(number - 1):
    if element[i] * element[i + 1] > 0:
        print("YES")
        break
else:
    print("NO")


#map คือ แปลงทุกตัวเป็นอะไรก็ได้