from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
def login(request):
    if request.method=='POST':
        form = AuthenticationForm(request=request, data=request.POST)
        #로그인 처리 요청
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:   # 로그인 화면요청
        #로그인 용 form 전달해주기
        if request.user.is_authenticated:   #이미 로그인 되어있다면
            return redirect('articles:index')   #인덱스 화면으로 이동
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.method=='POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        if request.user.is_authenticated:   #이미 로그인 되어있다면
            return redirect('articles:index')   #인덱스 화면으로 이동
        # 회원가입용 form 을 사용 >> UserCreationForm >> CustomUserCreationForm
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request,'accounts/signup.html',context)

def update(request):
    # POST, GET 요청 구분해서 GET 요청 화면 보여주기 
    # 3분
    if request.method == 'POST':
            # 원래 user정보랑, 사용자가 입력한 정보 같이 전달해주어야 합니다.
            form = CustomUserChangeForm(data=request.POST, instance = request.user)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
    else:
        # request.user   : 현재 로그인된 사용자 정보를 포함하는 User model instance
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form' : form
    }
    return render(request,'accounts/update.html',context)

def change_password(request,user_pk):
    # 비밀번호 변경할 수 있는 양식 보여주기
    # 실제 비밀번호 변경하기 
    if request.method=='POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        # form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            # 저장을 하게 되면 session 정보가 달라지기 때문에 세션이 무효화
            # 로그인 상태가 취소가 됨
            # 만약, 비밀번호 변경 후, 로그인을 유지하고 싶다면 세션 정보를 변경된 정보로 update
            # update_session_auth_hash >>> request에 있는 user 정보를 update
            update_session_auth_hash(request,user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {
        'form' : form
    }
    return render(request,'accounts/change_password.html',context)


