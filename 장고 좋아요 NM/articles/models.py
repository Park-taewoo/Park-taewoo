from django.db import models
from django.conf import settings

# 모델 선언 부분에서는 get_user_model() 함수를 사용하지 않음

# from django.contrib.auth import get_user_model
# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_articles')
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Article과 1:N의 관계를 가지는 Comment 클래스 작성하기
# 댓글은 어떤 게시글에 종속되어야 합니다.
# 댓글이 어느 게시글을 참조하는지 정의를 해야함
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # table에 존재하는 게시글만 참조되어야 합니다.
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
