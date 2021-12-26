quiz = {
   1 : {
       "question" : "What is the movie name of Iron Man in Avengers?",
       "answer" : "Tony Stark"
   },
   2 : {
       "question" : "Who is called the God of Lightning in Avengers?",
       "answer" : "Thor"
   },
   3 : {
       "question" : "Who carries a shield of American flag theme in Avengers?",
       "answer" : "Captain America"
   },
   4 : {
       "question" : "Which avenger is green in color?",
       "answer" : "Hulk"
   },
   5 : {
       "question" : "Which avenger can change it's size?",
       "answer" : "Ant Man"
   },
   6 : {
       "question" : "Which Avenger is red in color and has mind stone?",
       "answer" : "Vision"
   },
   7 : {
       "question" : "Who from avengers died at the end of Avengers:Endgame?",
       "answer" : "Iron Man"
   },
   8 : {
       "question" : "Who is called the Legend of Ten Rings?",
       "answer" : "Shang Chi"
   },
   9 : {
       "question" : "What was the name of Iron Man's latest AI computer program?",
       "answer" : "EDITH."
   },
   10 : {
       "question" : "What is the real name of Captain America?",
       "answer" : "Chris Evans"
   }
}


def check_ans(question, ans, attempts, score):

    if quiz[question]['answer'].lower() == ans.lower():
        score += 1
        print("\nCorrect Answer! \nYour score is ",score," !!!")
        return True
    else:
        attempts -= 1
        print("\nWrong Answer :( \nYou have ",attempts," attempts left! \nTry again !!!")
        return False


def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])



def quizgame():
    print("Welcome to this fun Marvel quiz!\nAre you ready to test your knowledge about MCU?\nThere are a total of 10 questions, you can skip a question anytime by typing 'skip'")
    input("Press any key to start the fun :)")
    while True:
        score = 0
        i = 1
        for question in quiz:
            attempts = 3
            while attempts > 0:
                print("\nQuestion ",i,": ",quiz[question]['question'])
                answer = input("Answer: ")
                if answer.lower() == "skip":
                    break
                elif answer == '0':
                    return
                check = check_ans(question, answer, attempts, score)
                if check:
                    score += 1
                    break
                attempts -= 1
            i += 1
        break
    print("\nYour final score is {score}!\n\n")
    print("Want to know the correct answers? Please see them below! :)\n")
    print_dictionary()
    print("\nThanks for playing! 💜")
