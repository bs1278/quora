from django.db import models
from django.contrib.auth.models import User
from questions.managers import  QuestionManager
from django.conf import settings
# Create your models here.


class TimeStamp(models.Model):
    """
    Reusable Abstract Timestamp Model Class.
    """
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        
            
    
class Question(TimeStamp):
    """
    Question model class.
    """
    question = models.CharField(max_length=100)
    asked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    is_answered = models.BooleanField(default=False)
    
    objects =  QuestionManager()
    
    def __str__(self):
        return self.question
    
    
    def answered(self):
        self.is_answered = True
        self.save(update_fields=['is_answered'])
    
    
class Answer(TimeStamp):
    """
    Answer model Class.
    """
    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE
    )
    answer = models.TextField()
    answer_by =models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True, blank=True
    )
    
    def __str__(self):
        return "{}".format(str(self.question))