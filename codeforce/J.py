number_of_minutes = int(input())
if number_of_minutes < 1440 :
    print(number_of_minutes // 60)
    print(number_of_minutes % 60)