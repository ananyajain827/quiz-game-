questions=("What shape has three sides?",
           "What is the capital of India?",
           "What is the name of the largest planet in our solar system?",
           "How many sides does a triangle have?",
           "What is the name of the house made of ice?")

options=(("A. circle","B. square","C. triange","D. cylinder"),
          ("A. delhi","B. mumbai","C. agra","D. gwalior"),
           ("A. saturn","B. jupiter","C. neptune","D. uranus"),
            ("A. 4","B. 7","C. 8","D. 3"),
             ("A. snow","B. igloo","C. hut","D. building"))

answers= ("C","A","B","D","B")
guesses=[]
ques_num=0
score=0

for question in questions:
     print("--------------------")
     print(question)
     for option in options[ques_num]:
          print(option)


     guess=input("enter only A,B,C or D\n").upper()
     guesses.append(guess)

     if guess==answers[ques_num]:
          score+=1
          print("CORRECT")
     else:
          print("INCORRECT")
          print(f"{answers[ques_num]} is the correct answer")

     ques_num += 1

print("\n\n------------RESULT-------------\n")

print("guesses:",end=" ")
for guess in guesses:
     print(f"{guess:5}",end=" ")

print("\nanswers:",end=" ")
for answer in answers:
     print(f"{answer:5}",end=" ")

print("\n\n-------------SCORE------------\n")
score=int(score/len(questions)*100)
print("your score",score)
if score<=30:
     print("better luck next time :(")
else:
     print("good work")
