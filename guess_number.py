from random import randint

count = 0
number = randint(1, 20)
print("Let's play a guessing game, number between 1 to 20")
while True:
    user_answer = int(input("The number is?"))
    count += 1
    if number == user_answer:
        print(f"GOOD JOB MY BUDDY!The answer is {number}!")
        print(f"You tried {count} times in total.")
        print("Thank You for playig this game my buddy")  
        break
    elif number > user_answer:
        print("TOO LOW")
    elif number < user_answer:
        print("TOO HIGH")
    # track down how many times did user tried
# count = count + 1 is same as count += 1
