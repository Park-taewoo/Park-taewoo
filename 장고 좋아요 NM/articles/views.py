from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_safe, require_POST, require_http_methods
# Create your views here.

@require_safe   # GET,HEAD 요청만 처리
def index(request):
    articles = Article.objects.all().order_by('-pk')    
    context= {
        'articles' : articles
    }

    return render(request,'articles/index.html',context)
# 로그인이 안되어있으면 accounts/login/ redirect
@login_required
@require_http_methods(['GET','POST'])
def create(request):    
    if request.method=='POST':
        form = ArticleForm(data=request.POST,files=request.FILES)
        if form.is_valid(): 
            article = form.save(commit=False) 
            article.user = request.user
            article.save()
            return redirect('articles:index')
        
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request,'articles/create.html',context)

@require_safe
def detail(request,pk):
    article =Article.objects.get(pk=pk)
    # 특정 게시글을 참조한는 댓글 조회하기 
    comments = article.comment_set.all()
    # comments = article.comments.all()
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request,'articles/detail.html',context)

@require_http_methods(['GET','POST'])
def update(request,pk):
    article = Article.objects.get(pk=pk)
    #로그인한 사용자와 게시글을 작성한 작성자가 같을 때만 로직 수행
    if request.user == article.user:
        if request.method == 'POST':
            
            form = ArticleForm(data=request.POST,instance=article)

            if form.is_valid():
                form.save()
                return redirect('articles:detail',pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'article' : article,
            'form' : form
        }
        return render(request,'articles/update.html',context)  
    return redirect('articles:detail',pk)

@require_POST
def delete(request,pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method=='POST':
        # pk에 해당하는 요소 table에서 삭제하기 
            article.delete()
            # 삭제 후에 인덱스 페이지로 돌아가기
    return redirect('articles:index')

@require_POST
def comment_create(request,article_pk):
    # 사용자가 입력한 내용으로 댓글 작성하고....
    form = CommentForm(data=request.POST)
    article = Article.objects.get(pk=article_pk)
    if form.is_valid():
        #form 안에 article 에 대한 정보가 비어있어서 NOT NULL 제약사항 위반
        # Comment Model instance는 article을 가지고 있음
        # form.save()는 모델 instance를 반환
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article_pk)
    # 화면은 게시글 상세 화면으로....

@login_required
def likes(request,article_pk):
    #현재 로그인한 유저가
    # article_pk 의 게시글을 좋아요 하기
    # article.like_users.add(user)
    # user.like_articles.add(article)
    article = Article.objects.get(pk=article_pk)
    # 1. 게시글을 좋아요 한 모든 사람을 조회 : article.like_users.all()
    # 2. 만약에 현재 로그인한 사람(request.user)이 목록에 없다면 좋아요 상태가 아닌거
    # article.like_users.all()
    #  article not in request.user.like_articles.all() 
    if request.user not in article.like_users.all(): #아직 좋아요가 아니라면
        # 좋아요 추가
        article.like_users.add(request.user)
    else:   #이미 좋아요 상태라면 취소
        # 좋아요 취소
        article.like_users.remove(request.user)
    # request.user.like_articles.add(article)
    return redirect('articles:index')
    