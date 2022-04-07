from components.quizQuestions import questions
from components import vars, quizTally
from PIL import Image

answer1 = questions["q1"][input(questions["q1"]["question"])]
vars.quizTotal += answer1
print("\n")

answer2 = questions["q2"][input(questions["q2"]["question"])]
vars.quizTotal += answer2
print("\n")

answer3 = questions["q3"][input(questions["q3"]["question"])]
vars.quizTotal += answer3
print("\n")

answer4 = questions["q4"][input(questions["q4"]["question"])]
vars.quizTotal += answer4
print("\n")

print("Total so far " + str(vars.quizTotal) + "\n")
quizTally.total(vars.quizTotal)
