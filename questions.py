# keeping class simple
class Question:
    """Base class for questions (str) and answers (ints/floats)"""
    answers = None
    text = None

class Add(Question):
    """Takes two numbers, adds them, then creates .text attribute of questions 
    and .answer attribute with answer.
    """
    def __init__(self, num1, num2):
        self.text = '{0} + {1}:'.format(num1, num2)
        self.answer = num1 + num2
    
class Multiply(Question):
    """Takes two numbers, multiplies them, then creates .text attribute of 
    questions and .answer attribute with answer.
    """
    def __init__(self, num1, num2):
        self.text = '{0} x {1}:'.format(num1, num2)
        self.answer = num1 * num2
