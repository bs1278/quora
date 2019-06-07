from django.shortcuts import render
from django.views.generic import TemplateView, ListView,DetailView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from questions.forms import CreateQuestionForm, AnswerForm
from questions.business_logics import CreateQuestion,QuestionAlreadyExistError,AnswerQuestion
from questions.models  import Question
# Create your views here.


class HomeView(ListView):
    model = Question
    template_name = 'home.html'
    context_object_name = 'questions'
    
    
home_view = HomeView.as_view()


class AnsweredQuestionsView(ListView):
    model = Question
    template_name ='answered_questions.html'
    context_obeject_name = 'questions'
    
    def get_queryset(self):
        queryset = Question.objects.answered_questions()
        return queryset

answered_questions_view = AnsweredQuestionsView.as_view()


class UnAnsweredQuestionsView(ListView):

    model = Question
    template_name = 'unanswered_Questions.html'
    context_object_name = 'questions'
    
    def get_queryset(self):
        queryset = Question.objects.unanswered_questions()
        return queryset

unanswered_questions_view = UnAnsweredQuestionsView.as_view()


class CreateQuestionView(LoginRequiredMixin,FormView):
    
    login_url = reverse_lazy('login_view')
    template_name = 'ask_question.html'
    form_class = CreateQuestionForm
    success_url = reverse_lazy('home_view')
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        
        if form.is_valid():
            self._run_business_logic(form)
            if not form.errors:
                return self.form_valid(form)
        return self.form_invalid(form)
    
    def _run_business_logic(self, form):
        question_business = CreateQuestion(
            form.cleaned_data['question'],
            self.request.user,
        )
        
        try:
            question_business.execute_question()
            
        except QuestionAlreadyExistError as err:
            form.add_error('question', str(err))
        
        
create_question_view = CreateQuestionView.as_view()


@login_required(login_url=reverse_lazy('login_view'))
def question_detail_view(request, pk):
    
    def _run_business_logic(question,answer_form, user):
        print("calling")
        print(question)
        print(answer_form.cleaned_data['answer'])
        print(user)
        answer_business = AnswerQuestion(
            question,
            answer_form.cleaned_data['answer'],
            user,
        )
#        answer_business.execute_answer()
        try:
            answer_business.execute_answer()
            print("f")
        except Exception as err:
            print("ff")
            pass
            
    question = get_object_or_404(Question, pk=pk)
   
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST or None)
        if answer_form.is_valid():
            print(question)
            _run_business_logic(question,answer_form,request.user)
            question.answered()
    
    answer_form = AnswerForm            
    return render(request, 'question_detail.html', {
        'answer_form':answer_form,
        'question':question}
                 )



def answer_view(request):
    answer = request.GET.get('answer', None)
    print(answer)
    return JsonResponse(data)