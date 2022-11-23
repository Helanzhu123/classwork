# import sixtyone

# result = sixtyone.circle_area(25)

# print(result)


#HOMEWORK!!!!!!
#CALCULATE THE AREA OF A TRIANGLE

# def tri_area(base:float, height:float)-> float:
#     answer = (base * height)/ 2
#     return answer
    
# answer = tri_area(10,20)
# print(answer)

# ex: central process unit, take the first letter of the words and compared them: CPU. Acronym/Abbrieation
#IMPORTANT
def acronym(sentence:str)-> str:
    y = ""
    sentence_list = sentence.split(" ")
    for word in sentence_list:
        y += word[0].upper() 
    return y

sentence = input("Your sentence: ")
x = acronym(sentence) #this is a return value
print(x)




