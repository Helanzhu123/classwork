from random import randint



print("----------   Math Test   ----------")
print()
score = 0
question_number = 0
for i in range(10):
    x = randint(1, 10)
    y = randint(1, 10)
    answer = int(input(f"{x} + {y}=?"))
    question_number += 1
    if answer == x + y:
        score += 10
        print(f"Correct! Addition of 10 points!")
    if answer != x + y:
        print(f"Answer is wrong but nice try.")
    elif question_number == 10:
        print(f"Good job mate! Here is your final score:{score}")
# There is still a bug exists