number = int(input())
element = input().split()


for index in range(number): # number = ขนาดของ element อยู่เเล้ว ดังนั้นเอามาใช้เเทน len ได้เลย
    element[index] = int(element[index])
    # print(element[index])

for index in range(number - 1): # เช็ก 4 รอบ เพราะว่าตัวปัจจุบันไปเช็กตัวด้านหน้า จนตัวสุดท้ายก็จะเช็กกับตัวก่อนหน้า
    if element[index] * element[index + 1] > 0:
        print("YES")
        exit()

print("NO")


#map คือ แปลงทุกตัวเป็นอะไรก็ได้