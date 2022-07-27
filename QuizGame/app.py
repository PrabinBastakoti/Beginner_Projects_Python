from Questions import a
question_prompt=[
    "What color are Apple?\n(a) Red/Green\n(b) Yellow\n(c) Brown\n\n",
    "What color are Banana?\n(a) Red/Green\n(b) Yellow\n(c) Brown\n\n", 
    "What color are Strawberries?\n(a) Red\n(b) Yellow\n(c) Brown\n\n"
]

hello=[
    a(question_prompt[0], "a"),
    a(question_prompt[1], "b"),
    a(question_prompt[2], "a")
] 



def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got " + str(score) + "/" + str(len(questions))+ " Correct")

run_test(hello)
