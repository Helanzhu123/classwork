# Built-in Functions, no need of import, and all data types can use it: https://docs.python.org/3/library/functions.html

import random

scores = []
for i in range(10):
    x = random.randint(0, 100)
    scores.append(x)
print(scores)
print(max(scores)) #print the highest
print(min(scores)) #print the lowest
hscore = 0
for i in scores:
    if i > hscore:
        hscore = i
print(hscore)       # also print the highest

lscore = 100
for u in scores:
    if u < lscore:
        lscore = u
print(lscore)       # also print the lowest

print("---------------")
#average of list
count = 0
for q in scores:
    count += q
print(q) #The last item
print(count)
print(count//len(scores)) #one divide with decimal

print("----------------")
print(sum(scores)//len(scores)) #also average of list

print("------------------")

print(scores.index(max(scores))) #locate the highest number

