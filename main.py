"""Using datetime to make an app that will ask us math questions
and time our answers.
"""
from quiz import Quiz
   
 
# create class to keep track of quiz scores over time?
def main():
    while True:
        quiz_prompt = input('Do you want a math quiz? y/n')
        if quiz_prompt.lower()[0] == 'y':
            quiz1 = Quiz() 
            quiz1.take_quiz() # start quiz
        elif quiz_prompt.lower()[0] == 'n':
            print('Ok. Goodbye')
            break
        else:
            print('Enter a valid input: y/n')
main()
