
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    #회원가입
    path('signup/', views.signup, name='signup'),
    # 회원정보수정
    path('update/', views.update, name='update'),
    
    #비밀번호 변경은 pjt/urls.py에서 처리
    
]