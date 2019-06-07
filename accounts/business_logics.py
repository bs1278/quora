from django.utils.translation import gettext as _

from accounts.models import UserAccount
from accounts.helpers import WelcomeEmail


class UsernameAlreadyExistError(Exception):
    pass


class CreateUserAccount:
    
    def __init__(self, 
                 username, 
                 email, password, 
                 first_name=None, 
                 last_name=None
                ):
        self._username = username
        self._email = email
        self._password = password
        self._first_name = first_name
        self._last_name = last_name
    
    def execute_data(self):
        self.valid_data()
        user_account = self._factory_user_account()
        self._send_welcome_email_to(user_account)
        return user_account
    
    def valid_data(self):
        # this is public method to allow clients of this object to validate
        
        user_account_qs = UserAccount.user_objects.find_by_username(self._username)
        if user_account_qs.exists():
            # Raise meaningful error to be catched by client
            
            error_msg = (
                'USER ALREADY EXISTS WITH {} USERNAME.'
                'please try another username'
            ).format(self._username)
            
            raise UsernameAlreadyExistError(_(error_msg))
        return True
    
    def _send_welcome_email_to(self, user_account):
        #WelcomeEmail.send_to([user_account.email])
        pass
    
    def _factory_user_account(self):
        # Factory to create an user account.
        # Ideally it would be implemented by useraccount manager.
        return UserAccount.user_objects.create_user(
            self._username,
            self._email,
            self._password,
            **{
                'first_name':self._first_name,
                'last_name':self._last_name
            }
        )