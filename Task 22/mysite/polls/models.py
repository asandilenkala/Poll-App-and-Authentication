from django.db import models
from django.utils import timezone
import datetime

# Define the Question model which represents a poll question
class Question(models.Model):
    # Text of the question, with a maximum length of 200 characters
    question_text = models.CharField(max_length=200)
    # Date and time when the question was published
    pub_date = models.DateTimeField('date published')

    # String representation of the Question model
    def __str__(self):
        return self.question_text

    # Check if the question was published recently (within the last day)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Define the Choice model which represents an answer to a poll question
class Choice(models.Model):
    # ForeignKey to the Question model, indicating which question this choice belongs to
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Text of the choice, with a maximum length of 200 characters
    choice_text = models.CharField(max_length=200)
    # Number of votes the choice has received, default is 0
    votes = models.IntegerField(default=0)

    # String representation of the Choice model
    def __str__(self):
        return self.choice_text

