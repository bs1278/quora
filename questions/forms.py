from django import forms
from django.utils.translation import gettext as _


class CreateQuestionForm(forms.Form):
    
    question = forms.CharField(required=True, widget=forms.Textarea)

    
class AnswerForm(forms.Form):
    
    answer = forms.CharField(widget=forms.Textarea)
   