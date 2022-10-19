from random import randint


number = randint(1, 20)
print("Let's play a guessing game, number between 1 to 20")
while True:
    user_answer = int(input("The number is?"))
    if number == user_answer:
        print(f"GOOD JOB MY BUDDY!The answer is {number}!")
        print("Thank You my buddy") 
        break
    elif number > user_answer:
        print("TOO LOW")
    elif number < user_answer:
        print("TOO HIGH")
    # track down how many times did user tried