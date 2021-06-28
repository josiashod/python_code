import random
import operator

NB_MIN = 1
NB_MAX = 50
NB_QUESTION = 4

operators = {
    '+': operator.__add__,
    '-': operator.__sub__,
    '*': operator.__mul__,
    '/': operator.__truediv__,
    '%': operator.__mod__,
}

def ask_question():
    a = random.randint(NB_MIN,NB_MAX)
    b = random.randint(NB_MIN,NB_MAX)
    operation = random.choice(list(operators.keys()))

    ok = False
    while not ok:
        answer = input(f"What is the result of {a} {operation} {b} ? ")

        try:
            answer = float(answer)
        except:
            print("This is not a number \n")
            continue
        else:
            ok = True
        
        correct_answer = round(operators[operation](a, b), 2)

    return answer == correct_answer

stop = False

while not stop:
    points = 0
    
    for i in range(NB_QUESTION):
        print(f"Question n°{i+1}/{NB_QUESTION}")
        if ask_question():
            print("Correct answer")
            points += 1
        else:
            print("Incorrect answer")
        
        print()

    moy = NB_QUESTION // 2
    
    if points == NB_QUESTION:
        print("excellent".upper())
    elif points == 0:
        print("You should seriously learn math".upper())
    elif points > moy:
        print("good job".upper())
    else:
        print("can do better".upper())

    print(f"You got : {points}/{NB_QUESTION}\n")

    ok = False
    while not ok:
        wish = input("Do you want to stop Y or N ? ")

        if wish.upper() not in ['Y', 'N'] or wish.isnumeric():
            print("Please choose the correct option")
        else:
            if wish.upper() == 'Y':
                ok = True
                stop = True
                print("bye bye !!")
            else:
                ok = True
                print()
