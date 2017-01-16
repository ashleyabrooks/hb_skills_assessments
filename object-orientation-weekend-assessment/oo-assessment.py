"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   1. Abstraction: Object orientation allows us to hide details we don't need by
   storing information about an object in its class attributes and methods. This way,
   we can simply call the object in a function rather than writing all of the 
   necessary attributes into the function itself. 

   2. Encapsulation: By creating a class, we're able to keep all information about 
   the object together in one place. It's easier to keep track of the info. 

   3. Polymorphism: Because classes can inherit from other parent classes, we can 
   use polymorphism and the super() method to manipulate the components for use in
   the subclass. 

2. What is a class?

    A class is a data structure that allows for storage of attributes and methods 
    related to the object. Once the class is defined, we can create instances of 
    the class with the same defined attributes and methods. 

3. What is an instance attribute?
    
    An instance attribute is an attribute that is stored only in the single instance
    of a class object. It allows us to manipulate the object in this one instance 
    without changing the class attributes. 

4. What is a method?
    
    A method is essentially a function defined within a class. With class methods, 
    we can define functions that can only be used with that specific class. 

5. What is an instance in object orientation?

    An instance is an individual occurrence of a class or object. An instance can 
    be as simple as a string 'ashley' (instantiating the string class).

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is an attribute defined for the entire class, while an instance
   attribute is only defined for that one instance. One might use a class attribute
   for a Watermelon class to say all watermelons have a green rind, but will use an
   instance attribute to say a specific instance (or type) of watermelon is seedless.


"""


"""Part 2 through 5"""

class Student(object):

    def __init__(self, first_name, last_name=None, address=None, score=0):
        self.name = first_name
        self.lastname = last_name
        self.address = address
        self.score = score

class Question(object):

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        print self.question 
        student_answer = raw_input('> ')
        
        if student_answer == self.correct_answer:
            return True
        else:
            return False

class Exam(object):

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        exam_question = Question(question, correct_answer)
        self.questions.append(exam_question)

    def administer(self, student):
        score = 0

        for question in self.questions:
            if Question.ask_and_evaluate(question) == True:
                score += 1

        print 'Your score is...'
        # python thinks 2 divided by 3 is 0 so multiplying by 100 first
        percentage_score = (score * 100) / len(self.questions)
        print percentage_score

class Quiz(Exam):

    def administer(self):
        percentage_score = super(Quiz, self).administer()
        
        if percentage_score >= 50:
            return True
        else:
            return False


def take_test(exam, student):
    score = exam.administer(student)
    return score


def example(exam, student):
    exam = Exam(exam)
    student = Student(student)

    exam.add_question("What is the CEO of Ubermelon's name?", "Mel")
    exam.add_question('Is a tuple mutable or immutable?', 'immutable')
    exam.add_question("Is the sky blue?", 'yes')

    take_test(exam, student)


