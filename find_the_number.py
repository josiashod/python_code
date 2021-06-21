from random import randint

print("""
************************************************************
*                 - Magic number Rules -                   *
* A random number is taken between 1 and 10 and you've 4   *
* try to take the right number                             *
*                                                          *
************************************************************
""")

lifes = 4
winning_number = randint(1, 10)
win = False
while lifes > 0 and not win:
    ok = False
    while not ok:
        try:
            user_number = input("What is the magic number : ")
            user_number = int(user_number)
        except ValueError:
            print("Error : Please enter a number")
            ok = False
            continue
        if user_number < 0 or user_number > 10:
            print("Error : The number should be between 1 and 10")
            ok = False
            continue
        
        else:
            lifes -= 1
            if user_number > winning_number:
                print("smaller")
            elif user_number < winning_number:
                print("higher")
            else:
                win = True
            ok = True
    if lifes > 0 and not win:
        print(f"{ lifes } remaining left \n")

if win:
    print("Congratulations ! You win.")
else :
    print("Game over ! You lose.")