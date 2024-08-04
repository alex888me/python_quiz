from django.core.management.base import BaseCommand
from home.models import Types, Question, Answer

class Command(BaseCommand):
    help = 'Add questions and answers to the database'

    def handle(self, *args, **kwargs):
        # Create a type
        gfg_type = Types.objects.create(gfg_name='Python Essentials 1')


        question = Question.objects.create(
            gfg=gfg_type,
            question=r'The \n digraph forces the print() function to:', marks=5)
        Answer.objects.create(question=question, answer=r'output exactly two characters: \ and n', is_correct=False)
        Answer.objects.create(question=question, answer=r'break the output line', is_correct=True)
        Answer.objects.create(question=question, answer=r'duplicate the character next to the digraph', is_correct=False)
        Answer.objects.create(question=question, answer=r'stop its execution', is_correct=False)

        question = Question.objects.create(
            gfg=gfg_type,
            question="What is the output of the following snippet?\n"
                     "z = y = x = 1\n"
                     "print(x, y, z, sep='*')", marks=5)
        Answer.objects.create(question=question, answer=r'x*y*z', is_correct=False)
        Answer.objects.create(question=question, answer=r'1 1 1', is_correct=False)
        Answer.objects.create(question=question, answer=r'x y z', is_correct=False)
        Answer.objects.create(question=question, answer=r'1*1*1', is_correct=True)


        """
        Python Essentials 1    Module 2
        Data types, variables, basic input-output operations, basic operators    
        how to write and run simple Python programs;
        what Python literals, operators, and expressions are;
        what variables are and what are the rules that govern them;
        how to perform basic input and output operations.
        
        python manage.py migrate
        python manage.py runserver
        python manage.py add_questions
        """

        self.stdout.write(self.style.SUCCESS('Successfully added questions and answers'))