"""Using datetime to make an app that will ask us math questions
and time our answers.
"""
from quiz import Quiz
    
    
def check_number_of_questions():
    # check if number
    while True:
        try:
            num_of_questions = int(input('How many questions do you want?'))
        except ValueError:
            print('Enter a valid whole number')
            continue
        break  # breaks if valid number is given.
    return num_of_questions
   
 
# create class to keep track of quiz scores over time?
def main():
    while True:
        quiz_prompt = input('Do you want a math quiz? y/n')
        if quiz_prompt.lower()[0] == 'y':
            num_of_questions = check_number_of_questions()
            quiz = Quiz(num_of_questions)  # start quiz
            quiz.take_quiz()
            
        elif quiz_prompt.lower()[0] == 'n':
            print('Ok. Goodbye')
            break
        else:
            print('Enter a valid input: y/n')
main()
