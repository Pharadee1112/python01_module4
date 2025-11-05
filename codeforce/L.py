first_chest = int(input())
second_chest = int(input()) 
third_chest = int(input())

min_chest = min(first_chest, second_chest, third_chest)
print((first_chest + second_chest + third_chest) - (min_chest))