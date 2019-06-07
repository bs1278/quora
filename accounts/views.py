from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView,DetailView

from accounts.forms import CreateUserAccountForm
from accounts.business_logics import CreateUserAccount,UsernameAlreadyExistError
from questions.models import Question
from django.contrib.auth import get_user_model
from accounts.models import UserAccount

class CreateUserView(FormView):
    
    template_name = 'registration.html'
    form_class = CreateUserAccountForm
    success_url = reverse_lazy('login_view')
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        
        if form.is_valid():
            # get the input and delegate to process
            self._run_business_logic(form)
            if not form.errors:
                return self.form_valid(form)
            
        return self.form_invalid(form)
    
    def _run_business_logic(self, form):
        
        business_logic = CreateUserAccount(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
        )
        
        # handle the output
        try:
            business_logic.execute_data()
        except UsernameAlreadyExistError as err:
            form.add_error('username', str(err))

create_user_view = CreateUserView.as_view()


class UserDetailView(DetailView):
    
    model = UserAccount
    context_object_name = 'user'
    template_name = 'user_detail.html'

user_detail_view = UserDetailView.as_view()