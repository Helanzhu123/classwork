#purple is key word
print("----------------------   WOW   ----------------------")
print()
print("Press 1 for singleplayer")
print("Press 2 for multiplayer")
while True:
    try:
        game_mode = int(input("Your choice: "))
        
        break
    except:
        print("Please insert 1 or 2")
        print("Please follow the rule")

try: 
    if game_mode == 1:
        print("Welcome to singleplayer mode")
    elif game_mode == 2:
        print("Welcome to multiplayer mode")
    elif game_mode == -1:
        raise "Thie exception is made by the author" #raise: throw an exception
    else:
        print("That is not a choice")
except:
    print("There is an error")