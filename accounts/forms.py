from django import forms
from django.utils.translation import gettext as _


class CreateUserAccountForm(forms.Form):
    
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput())
    
    def clean_confirm_password(self) -> str:
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        
        if confirm_password != password:
            raise forms.ValidationError(
                _("Password and Confirmation password must should be same")
            )
        
        return confirm_password