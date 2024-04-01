게시글(Article) CRUD
Model 
  Article
    title : 제목, 50글자 제한
    content : 내용
    created_at : 작성일  
    updated_at : 수정일

RESTful >>> 개발자들 끼리 약속. 개발 페러다임
        >>> 같은 기능인데 url 분리 말고method로 구분하자...
작성화면보여줘 
articles/create/   GET
DB에 저장해줘
articles/create/ POST




url
 /articles/      : 게시글 전체목록 조회 화면(메인화면)
 /articles/new/  : 게시글 작성화면
 /articles/create/ : 사용자가 입력한 게시글 DB에 저장
 /articles/<int:pk>/ : 특정 id를 가지는 게시글 상세보기 화면
 /articles/<int:pk>/modify/ : 게시글 수정화면(기존 게시글 내용포함)
 /articles/<int:pk>/update/ : 게시글 수정(DB 저장)

templates
   base.html
   index.html (메인화면, 게시글 목록출력)
   create.html (새 게시글 작성화면)
   update.html (게시글 수정화면)
   detail.html (게시글 상세화면)


ModelForm 만들기
  app > forms.py 생성

  form화면을 보여주기위한 요청처리 함수에서
  Article modelform instance 만들어서 template으로 전달
  template에서는 전달받은 form instance 이용해서 form 요소 출력

static 경로
app > static

파일업로드를 위해서 바꿔 주어야 되는 부분
1. form >> 인코딩 타입 변경 (파일 업로드를 할 수 있는 형태로)
   enctype="multipart/form-data"
2. views.py  : Model instance에 업로드 파일 설정
   form = ArticleForm(data=request.POST,files=request.FILES)
3. 업로드 경로 지정
  MEDIA_ROOT :  업로드 파일이 저장될 위치 지정
  MEDIA_URL : 업로드 파일에 접근하기 위한 URL경로 지정
  +
  Django project가 media url 처리할 수 있도록 urls.py 에
  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  추가

회원 관련 기능
로그인   
   1. 로그인 화면 보여줘 
   2. 로그인 처리해줘
로그아웃
<!-- 회원가입
회원정보수정
회원탈퇴 -->










