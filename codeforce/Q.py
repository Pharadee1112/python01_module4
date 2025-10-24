orange_cakes = int(input())
apple_cakes = int(input())

size_first_bags = int(input())
size_seocond_bags = int(input())

if orange_cakes <= size_first_bags and apple_cakes <= size_seocond_bags or \
    orange_cakes <= size_seocond_bags and apple_cakes <= size_first_bags :
    print("YES")

else :
    print("NO")
