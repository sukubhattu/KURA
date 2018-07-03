from accounts import views as accounts_views
from django.urls import path
#this below is for logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]