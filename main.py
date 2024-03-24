#-------------------------------------------------------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    options_guess = ['A', 'B', 'C', 'D','a','b','c','d']

    for question in questions:
        print("---------------------------------------------")
        print(question) # in all câu hỏi
        for i in options[question_num - 1]:
            print(i) # in option tương ứng với từng câu hỏi

        # Nhận input từ người dùng
        guess = ""
        while True:
            guess = input("Enter (A, B, C, or D): ").upper()
            
            if guess in options_guess:
                # Người dùng đã nhập đúng, thoát khỏi vòng lặp
                break
            else:
                print("Please re-enter")

        guesses.append(guess)
        
        # Lây đáp án (value) tương ứng của từng câu hỏi
        correct_guesses += check_answer(questions.get(question), guess)
        
        print("COORECT Guesses INPUT: ", correct_guesses)
        question_num += 1 # tăng chỉ số câu hỏi tương ứng

    display_score(correct_guesses, guesses)

#-------------------------------------------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0

    
#-------------------------------------------------------------------------------

def display_score(correct_guesses, guesses):
    print("---------------------------------------------")
    print("\t RESULTS")
    print("---------------------------------------------")
    print("Answer: ", end=" ")
    for ans in questions.values():
        print(ans,end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print(f"YOUR SCORE: {score}%")
#-------------------------------------------------------------------------------

def play_again():
    res = input("Do you want to play again?(Y/N): ").upper()

    if res == "Y":
        return True
    else:
        return False

#-------------------------------------------------------------------------------
def main():
    new_game()

    while play_again():
        new_game()

    print("Good bye ! Have a good time <3")

#-------------------------------------------------------------------------------

questions = {
    "1. Who created Python?: ": "A" ,
    "2. What year was Python created?: " : "B",
    "3. Python is tributed to which comedy group?: " : "C",
    "4. Where was Lalisa Manoban born?": "C",
}

options = [
    ["A. Guido van Rossum", "B. TheNghia_rr", "C. Bill Gates ", "D. Lalisa"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. FapTV", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. Viet Nam", "B. China", "C. ThaiLand", "D. USA"]
]

main()