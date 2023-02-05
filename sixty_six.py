#purple is key word
print("----------------------   WOW   ----------------------")
print()
print("Press 1 for singleplayer")
print("Press 2 for multiplayer")
while True:
    try:
        game_mode = int(input("Your choice: "))
        if game_mode == 1:
            print("Welcome to singleplayer mode")
            break
        elif game_mode == 2:
            print("Welcome to multiplayer mode")
            break
        elif game_mode == -1:
            raise "Thie exception is made by the author" #raise: throw an exception of your own
        else:
            print("That is not a choice")
    except ValueError as v_error: #this variable initialize the class #as: initialize a variable to a class
        print(v_error) #with_traceback: shows which line caused the error
    except NameError as n_error:
        print(f"{n_error} caught")
    except:
        print("Please insert 1 or 2")
        print("Please follow the rule")


#1. try 2. except 3. raise                #try and except must be together
