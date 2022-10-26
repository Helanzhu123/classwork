good_question = "how old are you???"
count = 0
for char in good_question:
    if char == "o":
        count += 1
print(count)


# good_question = "how old are you???"
# count = 0
# for char in good_question:
#     if char == " ":
#         count += 1
# print(count)

# index starts from 0 but starts at -1 from the other side, but len starts from 1

good_question = "how old are you??!"
pick = good_question[0]
pick_1 = good_question[1]
pick_2 = good_question[17]
pick_3 = good_question[len(good_question) -1]
pick_5 = good_question[-5]
print(pick, pick_1, pick_2, pick_3, pick_5)


