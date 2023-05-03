'''
Simple Quiz Program by Abraar | @retard.sonn

It is a open source program made for tutorials
'''

from art import *
import time


confirmation = input("\n\nAre you ready to play the Quiz? (Yes/No) : ").lower()

if confirmation == "yes" or confirmation == "y":
    tprint("Simple Quiz")

elif confirmation == "no" or confirmation == "n":
    print("Quiz cancelled as per user choice ...")
    time.sleep(2)
    exit()

else:
    print("ERROR: Input only 'Yes' or 'No'")
    exit()

time.sleep(2)

####################### Questions #####################
# Any user may add questions up to their choice..
q1 = '''Q1. What is the capital of India?

1. Dispur
2. Karnataka
3. Haryana
4. New Delhi

Answer: '''

q2 = '''Q2. Who is the Prime Minister of India?

1. Narendra Modi
2. Allubhai Patel
3. Himanta Bishwa Sharma
4. Rana Goswami

Answer: '''

q3 = '''Q3. What is the major language spoken in Assam?

1. Bodo
2. Bengali
3. Assamese
4. Hindi

Answer: '''

#################################################

######### Answers #####################
ans1 = "new delhi"
ans2 = "narendra modi"
ans3 = "assamese"
########################################

print("Questions will pop up soon ....".center(100))
print("NOTE: ANSWER ONLY IN WORDS! (NOT IN NUMBERS)\nEXTRAORDINARY ANSWERS WILL NOT BE ACCEPTED!".center(50))
time.sleep(5)

score = 0


input1 = input(q1).lower()
if input1 == ans1:
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

input2 = input(q2).lower()
if input2 == ans2:
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

input3 = input(q3).lower()
if input3 == ans3:
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

print("Checking Answers ...".center(100))
time.sleep(1)
print("Verifying Answers ...".center(100))
time.sleep(1)
print("Showing Results ...".center(100))
time.sleep(1)

if score == 3:
    print("Congrats! All of your answers are correct!")
elif score == 2:
    print("Good! Only 1 answer is incorrect..")
elif score == 1:
    print("You scored only 1 out of 3 :( !")
else:
    print("Better luck next time! All of your answers are incorrect!")
