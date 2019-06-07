"""quora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import create_user_view,user_detail_view
from questions.views import (home_view,
                             create_question_view,
                             question_detail_view,
                             answer_view,
                            answered_questions_view,
                            )

urlpatterns = [
    
    path('login', auth_views.LoginView.as_view(), {'template_name': 'login.html'}, name='login_view'),
    path('logout', auth_views.LogoutView.as_view(), name='logout_view'),    
    path('user-creation', create_user_view, name='user_creation_view'),
    path('user-details/<int:pk>/', user_detail_view, name='user_detail_view'),
    path('admin/', admin.site.urls),
    path('ask-question', create_question_view, name='create_question_view'),
    path(' answered_questions_view',  answered_questions_view, name='answered_questions_view'),
    path('question_detail_view/<int:pk>', question_detail_view, name='question_detail_view'),
    path('answer_view', answer_view, name='answer_view'),
   
    path('', home_view, name='home_view'),

]
