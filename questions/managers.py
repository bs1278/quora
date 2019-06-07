from django.db import models
from django.utils import timezone 


class QuestionQuerySet(models.QuerySet):

    def unanswered(self):
        now = timezone.now()
        return self.filter(is_answered=False, 
                           created_at__lte=now
                          )
    
    def answered(self):
        now = timezone.now()
        return self.filter(is_answered=True, 
                           created_at__lte=now
                          )
    
    
class QuestionManager(models.Manager):
    
    def find_by_question(self, question):
        queryset = self.get_queryset()
        return queryset.filter(question=question)
    
    def get_queryset(self):
        return QuestionQuerySet(self.model, using=self._db)
    
    def unasered_questions(self):
        return self.get_queryset().unanswered()
    
    def answered_questions(self):
        return self.get_queryset().answered()
    