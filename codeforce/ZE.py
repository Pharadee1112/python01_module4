won_in_game = input()

count_alice = 0
count_bob = 0

for character in won_in_game:
    if character == "A":
        count_alice += 1
    else :
        count_bob += 1

if count_alice > count_bob :
    print("ALICE")

elif count_alice < count_bob :
    print("BOB")

else:
    print("DRAW")