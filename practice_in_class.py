
print("よこそ僕のゲムに")



while True:
    print("Please choose a mini game")
    print()
    print("[1] Game One")
    print("[2] Game Two")

    choice = int(input("Choice: "))
    if choice == 1:
        print("Welcome to Game One")
        print("Please clap 5 times to win the game")
        while True: # Clapping Game
            print(f"Claps: {clap}")
            # menu options
            print("[1] Clap")
            # get choice
            choice = int(input("Choice: "))
            # handle choice
            if choice == 1:
                print("CLAP")
                clap = 0
            while clap < 5:
                print(f"Claps: {clap}")
                print("[1] Clap")
            print("You win the game! Congrat!")
    elif choice == 2:
        print("Welcome to Game Two")
