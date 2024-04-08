
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name ='detail'),
    path('<int:pk>/update/', views.update, name='update'), 
    path('<int:pk>/delete/', views.delete, name='delete'),
    # 댓글 추가
    path('<int:article_pk>/comment/', views.comment_create, name='comment_create'),
    #좋아요
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]