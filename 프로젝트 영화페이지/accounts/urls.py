
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    #회원가입
    path('signup/', views.signup, name='signup'),
    #회원정보수정
    path('update/', views.update, name='update'),
     #/1/password/ #프로젝트에서 처리
    # path('<int:user_pk>/password', views.change_password, name='change_password'),
    path('password/', views.change_password, name='change_password'),
]