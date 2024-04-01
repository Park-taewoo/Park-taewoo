from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
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
            form.save() 
            return redirect('articles:index')
        
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request,'articles/create.html',context)

def detail(request,pk):
    article =Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request,'articles/detail.html',context)


def update(request,pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
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


def delete(request,pk):
    if request.method=='POST':
    # pk에 해당하는 요소 table에서 삭제하기 
        article = Article.objects.get(pk=pk)
        article.delete()
        # 삭제 후에 인덱스 페이지로 돌아가기
        return redirect('articles:index')
    return redirect('articles:detail',pk)

    