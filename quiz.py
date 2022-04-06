from components.quizQuestions import questions
from components import vars, quizTally

answer1 = questions["q1"][input(questions["q1"]["question"])]
print(answer1)

vars.quizTotal += answer1
print("\n")

answer2 = questions["q1"][input(questions["q2"]["question"])]
print(answer2)

vars.quiztotal += answer2
print("\n")

print("Total so far " + str(vars.quizTotal) + "\n")
quizTally.total(vars.quizTotal)