# Day 3: Treasure Island Project
print("Welcome to Treasure Island.\nYour goal is to find the treasure.")

choice1 = input("You got out of your house. Do you want to go to the woods or to the lake?\nwoods or lake\n ").lower()
if choice1 == "woods":
    choice2 = input("You're in the lake. Do you want to take the boat or walk by the shore?\nboat or walk\n ").lower()
    if choice2 == "walk":
        choice3 = input("You reached the end of the beach and see a cabin. Do you want to enter the cabin or go to the garden?\ncabin or garden\n").lower()
        if choice3 == "cabin":
            choice4 = input("You're inside the cabin. You see 3 boxes. Do you want to open the red box or blue box or black box?\nred, black or blue\n ").lower()
            if choice4 == "red":
                print("You found the treasure! You Win!")
            elif choice4 == "black":
                print("It's just a rock. Game Over.")
            else:
                print("It's a time bomb. Game Over")
        else:
            print("You've been bitten by a venom snake. Game Over.")
    else:
        print("The boat is sinking. Game Over.")
else:
    print("There are wolves in the woods. Game Over.")
    