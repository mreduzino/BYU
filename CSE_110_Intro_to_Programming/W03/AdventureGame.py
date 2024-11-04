#Author: MReduzino

'''
Extra Points: I asked the player name to make the game more personal in the welcome message.
I showed the game to my Sister Giovanna and my Friend Matheus. The liked it and I explained the if/elif/else statements to them.
'''

player_name = input("Before we start, what's your name, brave adventurer? ")
print(f"Welcome to the forest decision game, {player_name}!\nBe wise on your choices!")

choice_1 = input("You are walking in a forest, and you see a cave, do you want to ENTER or GO AWAY? ")

if choice_1.lower() == "enter":
    print("There are two paths, do you want the RIGHT one or the LEFT one?")    
    choice_2_1 = input("Do you want to go RIGHT or LEFT? ")
    
    if choice_2_1.lower() == "right":
        print("There is a huge crack on the floor, do you want to JUMP, EXPLORE or TURN BACK? ")
        choice_3_1 = input("Do you want to JUMP, EXPLORE or TURN BACK? ")
        
        if choice_3_1.lower() == "jump":
            print("You jumped across and found a treasure! You won!")
        elif choice_3_1.lower() == "explore":
            print("You found a safe path around. You survived!")
        elif choice_3_1.lower() == "turn back":
            print("You went back safely. Nothing gained, nothing lost.")
        else:
            print("Invalid choice! Game Over!")
            
    elif choice_2_1.lower() == "left":
        print("You find a sleeping bear, do you want to SNEAK or RUN? ")
        choice_3_2 = input("What will you do? SNEAK or RUN? ")
        
        if choice_3_2.lower() == "sneak":
            print("You managed to sneak past the bear. You survived!")
        elif choice_3_2.lower() == "run":
            print("The bear woke up and caught you. Game Over!")
        else:
            print("Invalid choice! Game Over!")
    else:
        print("Invalid choice! Game Over!")

elif choice_1.lower() == "go away":
    print("You found a goblin, he asked if you want to FOLLOW HIM or KEEP WALKING? ")    
    choice_2_2 = input("What will you do? FOLLOW HIM or KEEP WALKING? ")
    
    if choice_2_2.lower() == "follow him":
        print("The goblin leads you to his home. Do you want to STAY or LEAVE? ")
        choice_3_3 = input("What will you do? STAY or LEAVE? ")
        
        if choice_3_3.lower() == "stay":
            print("The goblin shares his treasure with you. You won!")
        elif choice_3_3.lower() == "leave":
            print("You left safely. Nothing gained, nothing lost.")
        else:
            print("Invalid choice! Game Over!")
    
    elif choice_2_2.lower() == "keep walking":
        print("You got lost in the forest. Game Over!")
    else:
        print("Invalid choice! Game Over!")
else:
    print("Invalid choice! Game Over!")