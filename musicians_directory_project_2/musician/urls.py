from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.userSignup, name='signUp_page'),
    path('login/', views.UserLoginView.as_view(), name='login_page'),
    path('logout/', views.UserLogoutView.as_view(), name='logout_page'),
    path('add/', views.add_musician, name='add_musician'),
    path('edit/<int:id>', views.edit_musician, name='edit_musician'),
]