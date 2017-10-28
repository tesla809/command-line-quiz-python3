import datetime
import random

# the single space to to create visual seperation
# so, that I know which are built into the standard library (datetime, random)
# and which are my own custom ones.
from questions import Add, Multiply


class Quiz:
    """Creates and runs quiz with 10 questions"""
    questions = []  # Store and hold on to all the questions
    answers = []   # holds if they got questions right or wrong
    
    # Note: calling a attribute within class requires self.attribute
    def __init__(self, num_of_questions=10):
        """Generate 10 random questions with numbers from 1 to 10.
        Takes in type int for number questions.
        Default of num_of_questions is 10.
        """
        question_type = (Add, Multiply)
        for _ in range(num_of_questions):  # generate 10 random questions
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            # we get random number from question_type tuple
            # random.choice picks random element from population
            question = random.choice(question_type)
            
            # append random type of question
            self.questions.append(question(num1, num2))
    
    @staticmethod    
    def _time_passed(start, end):
        """Returns elapsed time between start and end"""
        return end - start
        
    @staticmethod
    def _format_time(datetime_obj):
        """Formats and returns times as strings"""
        time = datetime_obj.strftime('%I:%M:%S %p')
        time_rounded = time
        return time_rounded
    
    @staticmethod
    def _format_time_elapsed(time_delta):
        # Note: timedelta.min is not minutes, its minimum
        seconds_passed = time_delta.seconds
        minutes_passed = 0
        if seconds_passed >= 60:
            minutes_passed = int(seconds_passed / 60)
            seconds_passed %= 60
        if seconds_passed < 10:  # add leading zero to make it look correct
            seconds_passed = '0' + str(seconds_passed)
        result = '{}:{}'.format(minutes_passed, seconds_passed)
        return result

    def ask(self, question):
        start_time = datetime.datetime.now()  # gets the start time
        answer_time = None
        answer = None
        
        # makes sure that valid input is submitted: only int
        while answer != int:
            try:
                answer = int(input(question.text))  # capture the answer
                break  # if valid break
            except ValueError:
                print('Invalid entry. Enter only integers.')

        if answer == question.answer:  # check the answer
            end_time = datetime.datetime.now()  # log the end time
            answer_time = self._time_passed(start_time, end_time)
            # if the answer is right, return True and elapsed time.
            return True, answer_time
        else:
            end_time = datetime.datetime.now()
            answer_time = self._time_passed(start_time, end_time)
            # if answer is wrong, return False and elapsed time.
            return False, answer_time 

    def _summary(self, total_time):
        """Prints how many you got right and total # of questions,
        as well as the total time for quiz.
        """
        # prints how many you got right and total # of questions: 5/10
        score_counter = 0
        num_of_questions = len(self.questions)
        
        # tallies score
        for el in self.answers:
            result = el[0]
            if result == True:
                score_counter += 1
        print('Score: {0}/{1}'.format(score_counter, num_of_questions))
        
        # log if perfect score
        if score_counter == num_of_questions and num_of_questions != 0:  
            print('Perfect score!')
        
        # format and print the total time for quiz.
        total_time = self._format_time_elapsed(total_time)
        print('Total Quiz Time: {0}'.format(total_time))
    
    def take_quiz(self):
        """Method that asks the quiz questions"""
        total_quiz_time = None
        
        # quiz start
        quiz_start = datetime.datetime.now()
        quiz_start_log = self._format_time(quiz_start)
        print('Quiz starts at: {0}'.format(quiz_start_log)) # log start time
        
        # ask all of the questions
        for question in self.questions:
            answer = self.ask(question)
            is_correct, time_to_answer = answer
            time_to_answer = self._format_time_elapsed(time_to_answer)
            
            # feedback: correct or not
            if is_correct:   
                print('Correct. \nTime: {0}\n'.format(time_to_answer))
            else: 
                print('Nope. \nTime: {0}\n'.format(time_to_answer))
                
            self.answers.append(answer)  # add to self.answers list
        
        # quiz end    
        quiz_end = datetime.datetime.now()
        quiz_end_log = self._format_time(quiz_end)
        print('Quiz ended at: {0}\n'.format(quiz_end_log)) # log end time
        
        # total quiz time
        total_quiz_time = self._time_passed(quiz_start, quiz_end)
        
        # show a summary- call summary here
        self._summary(total_quiz_time)
        return '\nThanks for playing'
