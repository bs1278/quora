from django.contrib.auth.models import AbstractUser, UserManager


class UserAccountManager(UserManager):
    
    def find_by_username(self, username):
        queryset = self.get_queryset()
        return queryset.filter(username=username)
