from django.core.management.base import BaseCommand
from home.models import Types, Question, Answer

class Command(BaseCommand):
    help = 'Add questions and answers to the database'

    def handle(self, *args, **kwargs):
        # Create a type
        gfg_type = Types.objects.create(gfg_name='General Knowledge')

        # Create a question
        question = Question.objects.create(gfg=gfg_type, question='What is the capital of France?', marks=5)

        # Create answers
        Answer.objects.create(question=question, answer='Paris', is_correct=True)
        Answer.objects.create(question=question, answer='Berlin', is_correct=False)
        Answer.objects.create(question=question, answer='Madrid', is_correct=False)
        Answer.objects.create(question=question, answer='Rome', is_correct=False)

        self.stdout.write(self.style.SUCCESS('Successfully added questions and answers'))
