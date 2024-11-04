friends = []

new_friend = ""

while new_friend.lower() != "end":
    new_friend = input("Type the name of a friend: ")
    if new_friend.lower() != "end":
        friends.append(new_friend)
 
print("\nYour friends are:")
            
for friend in friends:
    print(friend)