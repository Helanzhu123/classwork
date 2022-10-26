from random import randint


print("----------   Math Test   ----------")
print()
x = randint(1, 10)
y = randint(1, 10)
score = 0
for i in range(10):
    answer = int(input(f"{x} + {y}=?"))
if answer == x + y:
    score += 10
    print(f"Correct! Addition of 10 points! Your current mark is {score}")
else:
    print("Answer is wrong but nice try")