print("Tommy was taking a vacation to Australia in a plane.")
print("But he had an option to bring an item before he went to Australia.")
choice1 = input("Should he pick skittles, starbucks coffee, a pocket knife, or pepper spray?")
choice2 = input("Does Tommy want to stay in the plane or leave it?")
if (choice2 == "stay"):
    print("Tommy chooses to stay on the plane, but a giant spider soon jumps out of nowhere and kills him.")

elif (choice2 == "leave"):
    print("Tommy jumps out of the plane and tries looking for any other passengers, and comes across a giant spider")

    if (choice1 == "starbucks coffee"):
        print("You died from a caffeine overdose.")

    else:
        choice3 = input("Should Tommy fight the spider or run and try to find any other survivors?")

        if (choice3 == "fight"):
            print("")

        if (choice3 == "run"):
            print("")
