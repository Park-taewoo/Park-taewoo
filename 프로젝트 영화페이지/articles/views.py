from django.shortcuts import render,redirect
from .models import Article,Comment
from .forms import ArticleForm,CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-pk')    
    context= {
        'articles' : articles
    }

    return render(request,'articles/index.html',context)

#로그인이 안되어있으면 로그인으로 바뀜
@login_required
def create(request):    
    if request.method=='POST':

        form = ArticleForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            # form.save()
            article = form.save(commit=False) 
            article.user=request.user
            article.save()
            return redirect('articles:index')
        
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request,'articles/create.html',context)

def detail(request,pk):
    article =Article.objects.get(pk=pk)
    comments=article.comments.all()
    comment_form=CommentForm()
    context = {
        'comments':comments,
        'article' : article,
        'comment_form' :comment_form,
    }
    return render(request,'articles/detail.html',context)


def update(request,pk):
    article = Article.objects.get(pk=pk)
    #로그인한 사용자와 게시글을 작성한 작성자가 같을때만 로직수행
    if request.user == article.user:
        if request.method == 'POST':
            # article = Article.objects.get(pk=pk)
            form = ArticleForm(data=request.POST,instance=article)

            if form.is_valid():
                form.save()
                return redirect('articles:detail',pk)
            
        else:
            article =Article.objects.get(pk=pk)
            form = ArticleForm(instance=article)
        context = {
            'article' : article,
            'form' : form
        }
        return render(request,'articles/update.html',context) 
    return redirect('articles:detail',pk)

def delete(request,pk):
    article = Article.objects.get(pk=pk)
    if request.user== article.user:
        if request.method=='POST':
        # pk에 해당하는 요소 table에서 삭제하기 
            # article = Article.objects.get(pk=pk)
            article.delete()
            # 삭제 후에 인덱스 페이지로 돌아가기
            return redirect('articles:index')
        return redirect('articles:detail',pk)
    return redirect('articles:detail',pk)

def comment_create(request,article_pk):
    #사용자가 입력한 내용으로 댓글 작성하고....
    comment_form = CommentForm(data=request.POST)#댓글
    article=Article.objects.get(pk=article_pk)#게시글
    comments=article.comments.all()
    if comment_form.is_valid():
        #form 안에 article에 대한 정보가 비어 있어서 NOT NULL 제약사항 위반
        # Comment Model instance는 article을 가지고 있음
        # form.save()는 모델 instance를 반환
        comment=comment_form.save(commit=False)
        comment.article=article
        comment.save()
        return redirect('articles:detail',article_pk)
    # 화면은 게시글 상세 화면으로
    context = {
        'comments' : comments,
        'comment_form' : comment_form,
        'article' : article
    }
    return render(request, 'articles/detail.html',context)
    