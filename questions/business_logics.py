from django.utils.translation import gettext as _
from questions.models import Question,Answer


class QuestionAlreadyExistError(Exception):
    pass


class CreateQuestion:
    
    def __init__(self, question, user):
        # set interanl state for class instance.
        self._question = question
        self._user = user
        
    def execute_question(self):
        self.valid_data()
        question_instance = self._question_factory()
        return question_instance

    def valid_data(self):
        question_qs = Question.objects.find_by_question(self._question)
        if question_qs.exists():
            error_msg = (
                'QUESTION ALREADY EXISTS'
            ).format(self._question)
            raise QuestionAlreadyExistError(_(error_msg))
        return True
    
    def _question_factory(self):
        # factory to create questions.
        return Question.objects.create(
            question=self._question,
            asked_by=self._user,
        )

    
class AnswerQuestion:
    
    def __init__(self, 
                 question, 
                 answer, 
                 answer_by):
        
        self._question = question
        self._answer = answer
        self._answer_by = answer_by
    
    
    def execute_answer(self):
        #self.valid_data()
        answer_instance = self._answer_factory()
        return answer_instance
    
    def valid_data(self):
        return True
    
    def _answer_factory(self):
        # factory to crerate answers.
        return Answer.objects.create(
            question=self._question, 
            answer=self._answer, 
            answer_by=self._answer_by
        )