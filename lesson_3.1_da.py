from random import randint


x = randint(1, 100)
y = randint(1, 100)
answer = int(input(f"{x} * {y}=?") )
correct_answer = x * y
if answer == correct_answer:
    print("good job")
else:
    print("try again")

