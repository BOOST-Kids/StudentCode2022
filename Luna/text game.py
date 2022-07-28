print("Tommy was flying on his flight to Australia")
print("He had a choice of items to bring with him")
choice1 = input("Does he pick the pocketknife, pepper spray, coffee, or skittles?")
print("the plane crashes into a tree")
choice2 = input("Do you stay on the plane or leave?")

if (choice2 == "stay"):
    print("You choose to stay on the plane. The spider creeps up on you and you DIE.")
    print("Game Over")

elif (choice2 == "leave"):
    print("storyline b")

    if (choice1 == "coffee"):
        print("Game Over")

    else:
        choice3 = input("Do you choose to fight the spider or run and try to find people?")

        if (choice3 =="fight"):
            print("Game Over")

        if (choice3 == "run"):
            print("")