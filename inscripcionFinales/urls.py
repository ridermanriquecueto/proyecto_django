from re import template
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import (HomePageView,CustomLoginView,CustomLogoutView,
    profileviews,registerView,carreraView,listUser,editUser,deleteUser, showUser)

from .views import (lista_materias)
    
from django.contrib.auth import views as auth_views, views

from django.contrib.auth.decorators import login_required





urlpatterns = [
      
    path('', HomePageView.as_view(), name= 'inicio'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("recover_pass/",auth_views.PasswordResetView.as_view(template_name="registration/recuperar_pass.html"),name='Recuperar Contraseña'),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_send.html"), name='password_reset_done'),
    path("create_user/",login_required(registerView.as_view(template_name= 'registration/register.html')), name='register'),
    path("career/", login_required(carreraView.as_view(template_name= 'carrera.html')), name='carrera'),
    path("institut/", login_required(carreraView.as_view(template_name= 'instituto.html')), name='instituto'),
    path("show_profile/", login_required(profileviews.as_view(template_name= 'registration/profile.html')), name='profile'),
    path("change_password/", auth_views.PasswordChangeView.as_view(template_name = 'registration/change_password.html'),name = 'change_password'),
    path("change_password_done/",auth_views.PasswordChangeDoneView.as_view(template_name='registration/success_password.html'), name='password_change_done'),
    path("user_list/",login_required(listUser.as_view(template_name='registration/list_user.html')),name='list_user'),
    path("edit_user/<int:pk>",login_required(editUser.as_view(template_name = 'registration/edit_profile.html')), name='edit_profile'),
    path("delete_user/<int:pk>",login_required(deleteUser.as_view(template_name='registration/delete_user.html')),name='delete_user'),
    path("show_user/<int:pk>",login_required(editUser.as_view(template_name = 'registration/show_user.html')), name='show_user'),
    path('lista_materias/', lista_materias, name='lista_materias'),
    #path('inscribirse_materia/<int:materia_id>/', inscribirse_materia, name='inscribirse_materia'),
]

