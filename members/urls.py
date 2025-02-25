from django.contrib import admin
from . import models, views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from .views import ( UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView,
                     CreateProfilePageView
                     )

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_settings', UserEditView.as_view(), name='edit_settings'),
    path('password/', PasswordsChangeView.as_view()),
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show-profile'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit-profile-page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create-profile-page'),

]

urlpatterns += staticfiles_urlpatterns()