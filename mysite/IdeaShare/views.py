from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt

#-----------------------------------기반 함수--------------------------------------------------------------------#

#templates이후 save_dir(/경로)를 입력하면 해당 파일 생성
def save_html(HTML_file,save_dir):
    saved_url='C:/Users/ebzma/anaconda3/envs/Assignment/cs2/mysite/IdeaShare/templates'
    with open (f'{saved_url}/{save_dir}','w',encoding="UTF-8-sig")as f:
        f.write(HTML_file)

#초기 HTML 모듈
def HTML_Template(head='',body='',articleTag='',start_html=''):
    return f'''
    {start_html}
    <!DOCTYPE html> 
    <html lang="ko"> 
    <head>
        {head}
    </head>
    <body style="background-color:#f2f2f2">
        {body}
        {articleTag}
        {{%block insert%}}
        {{%endblock%}}
    </body>
    </html>
    '''    

#가입,로그인 에러창 html 
def HTML_Error_Template(link,block_name,key):
    #에러창
    def make_assert(article):
            return f'''
            <div class="alert alert-danger d-flex align-items-center my-3" role="alert">
                <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Danger:"><use xlink:href="#exclamation-triangle-fill"/></svg>
                <div>
                {article}
                </div>
            </div>'''

    html_data=f'''
    {{% extends "{link}" %}}
    {{%block {block_name}%}}    
    '''
    for k in key:
        if key[k][0]==1:
            html_data+=make_assert(key[k][1])
    html_data+='''
    {%endblock%}
    '''
    return html_data

#-----------------------------------변수 및 전처리---------------------------------------------------------------#

#공통전역변수
start_url='' #뭔가 있으면 /index 이런식으로 서술
Global_key={'login':0}

#DB 불러오기
from .models import user_data,category_data

#-----------------------------------실질적인 코딩----------------------------------------------------------------#

#타이틀 html(str) 생성
def Title_Template(articleTag):
    global start_url, Global_key
    #헤드데이터
    header='''
    <meta charset="UTF-8-sig"> 
    <title>index</title> 

    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
    '''
    #카테고리 정보
    c_datas=category_data.objects.all().values()   

    #카테고리
    category_list=''
    for c_data in c_datas:

        category_list+=f'''<li><a class="dropdown-item" href="{start_url}/category/{c_data['id']}/">{c_data['category_name']}</a></li>
        '''
    #이미지 사용
    start_html='{% load static %}' 
    image_bulb_url="{%static 'images/lamp.png'%}"
    image_url="{%static 'images/logo_is.png'%}"
    style='style="background-color:#ffffff"'
    #타이틀 공통 HTML자료
    title=f'''
    <!--타이틀-->
    <nav class="navbar navbar-expand-lg navbar-light" {style}>
            <!--타이틀 내부 컨테이너-->
            <div class="container-lg">
                <!--제목-->
                <a class="navbar-brand" href="{start_url}/">
                    <img class= 'mb-2' src="{image_bulb_url}" alt="" width="30" >
                    IdeaShare
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <!--접히기-->
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                
                    <!--검색-->
                    <form class="d-flex mx-auto mb-2 mb-lg-0">
    '''
    if Global_key['login']==1:
        title+=f'''
                        <input class="form-control me-2 mr-2" type="search" placeholder="Search" aria-label="Search">
                        <button class="btn btn-outline-success" type="submit">Search</button>
                        <a href='/logout/'><button class="btn btn-outline-secondary" type="button">Logout</button></a>
                    
    
        '''
    title+=f'''
                    </form>
                    <!--목차-->
                    <form class="d-flex ml-auto">
                    <ul class="navbar-nav mb-2 mb-lg-0" style="width: 150px">
    '''
    
    if Global_key['login']==1:
        title+=f'''
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Category
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            {category_list}
                        </ul>
                    </li>
    '''
    title+=f'''
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        고객지원
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <li><a class="dropdown-item" href="{start_url}/service/FAQ">FAQ</a></li>
                        <li><a class="dropdown-item" href="{start_url}/service/GG">건의게시판</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="{start_url}/service/seh">Something else here</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{start_url}/Contact/">Contact</a>
                    </li>
                    </ul>
                    '''
    title+=f''' 
                </form>
                </div>
            </div>
        </nav>
    '''  

    #본론
    html_data=HTML_Template(head=header,body=title,articleTag=articleTag,start_html=start_html)
    return html_data

#초기화면       //생성html 
def index(request):
    image_url="{%static 'images/logo_is.png'%}"
    url="{% url 'IdeaShare:login' %}"
    blocks_s_login='{% block login %}'
    blocks_e='{%endblock%}'
    
    article=f'''
    <div class="container-lg">
        <div class="row pt-5">
            <!--image-->
            <div class="col-lg-5 ml-auto mr-auto mt-5">
                <img src="{image_url}" >
            </div>
            <div class="col-lg-7 mx-auto">
            
                <div class="row justify-content-end pt-5 text-center">
                    <H1>당신의 상상을 공유하세요!</H1>
                </div>
                <div class"row">
                    {blocks_s_login}
                    <ul class="navbar-nav">
                        <li class="nav-item ">
                            <a class="nav-link text-center" href="{url}">로그인</a>
                        </li>
                    </ul>
                    {blocks_e}
                </div>
            </div>
        </div>
    </div>
    '''
    HTML_file=(Title_Template(article))
    save_html(HTML_file,"title/title.html")    
    
    return render(request,"title/title.html")
    

#-----------------------------------가입,로그인,아웃-------------------------------------------------------------#
#로그인 창      //html
def login(request):
    global start_url
    return render(request,"Join_Login/login.html",{'start_url':start_url})
#로그인 실행    //html + 생성html
def dologin(request):
    global start_url,Global_key
    if request.method=='POST':
        #입력된값
        data=request.POST
        
        #print(data)    #검토용
        #-----------------------------------------------------------------------------#
        match={
            'useremail':'empty_email',
            'password':'empty_PW',
        }
        key={
            'empty_email':[0,'이메일을 입력해주세요.'],
            'empty_PW':[0,'PW를 입력해주세요'],
            }
            
        #-----------------------------------------------------------------------------#
        #error 체크
        #빈값
        count=0
        for i in match.items():
            if data[i[0]]=='':
                count=1
                key[i[1]][0]=1
        if count==1:
            link="Join_Login/Error_login.html"
            block_name="Error_login_ect"
            save_dir="/Join_Login/Error_login_ect.html"
            save_html(HTML_Error_Template(link,block_name,key),save_dir)
            return render(request,"Join_Login/Error_login_ect.html")
                
        #-----------------------------------------------------------------------------#
        #둘중하나 틀림
        
        if not(user_data.objects.filter(email=data['useremail']).exists()):
            return render(request,"Join_Login/Error_login.html")
        elif not(user_data.objects.filter(email=data['useremail'],password=data['password']).exists()):
            return render(request,"Join_Login/Error_login.html")
        
        #-----------------------------------------------------------------------------#
        
        Global_key['login']=1

        #출력될 아이디
        email=data['useremail']
        nickname=user_data.objects.filter(email=email).values('nickname')[0]['nickname']
        user_id=user_data.objects.filter(email=email).values('id')[0]['id']
        url=f'/blog/{user_id}/'

        return render(request,"Join_Login/success_login.html",{'start_url':start_url,'url':url,'nickname':nickname})
        #-----------------------------------------------------------------------------#

    return render(request,"Join_Login/login.html",{'start_url':start_url})

#가입 창        //html
def join_site(request):
    global start_url
    return render(request, "Join_Login/Join.html",{'start_url':start_url})
#가입 실행      //html + 생성html
def doJoin(request):
    global start_url,Global_key
    if request.method=='POST':
        #입력된값
        data=request.POST
        
        #검토
        match={
            'nickname':'empty_nickname',
            'useremail':'empty_email',
            'password':'empty_PW',
            'passwordcheck':'empty_PW_check',
            'hint':'empty_hint',
        }
        match_radio={
            'classes' : 'empty_classes',
            'gender':'empty_gender',
        }

        key={
            #미입력
            'empty_classes':[0,'계정종류를 선택해주세요.'],
            'empty_nickname':[0,'닉네임을 입력해주세요.'],
            'empty_email':[0,'이메일을 입력해주세요.'],
            'empty_PW':[0,'PW를 입력해주세요.'],
            'empty_PW_check':[0,'PW확인을 입력해주세요.'],
            'empty_hint':[0,'비밀번호힌트를 입력해주세요.'],
            'empty_gender':[0,'성별을 선택해주세요.'],
            #불일치
            'not_correct':[0,'비밀번호가 일치하지않습니다.'],
            #불만족
            'dissatisfied_minimum':[0,'비밀번호를 8자리이상 입력해주세요.'],
            #중복
            'duplicated_nickname':[0,'이미 사용된 닉네임입니다. 다른 닉네임을 사용해주세요.'],
            'duplicated_email':[0,'이미 사용된 email입니다. 다른 email을 사용해주세요.'],
            #할당초과
            'overflow_nickname':[0,'닉네임은 10자 이내로 작성해주십시오.'],
            'overflow_hint':[0,'힌트는 20자 이내로 작성해주십시오'],
            }
        #-----------------------------------------------------------------------------#
        #error 체크
        count=0
        #입력값이 빈경우
        for i in match.items():
            if data[i[0]]=='':
                count=1
                key[i[1]][0]=1
        #radio체크가 안된경우
        for i in match_radio.items():
            if not(i[0] in data.keys()):
                count=1
                key[i[1]][0]=1
        #비밀번호 불일치
        if data['password']!=data['passwordcheck']:
            key['not_correct'][0]=1
            count=1
        
        #중복체크
        if user_data.objects.filter(nickname=data['nickname']).exists():
            key['duplicated_nickname'][0]=1
            count=1
        if user_data.objects.filter(email=data['useremail']).exists():
            key['duplicated_email'][0]=1
            count=1

        #데이터사이즈 초과시
        #user_data.objects.create_user
        if len(data['nickname'])>10:
            key['overflow_nickname'][0]=1
            count=1
        if len(data['hint'])>20:
            key['overflow_hint'][0]=1
            count=1
        #-----------------------------------------------------------------------------#
        #최종출력(에러시)
        if count==1:
            link="Join_Login/Error_Join.html"
            block_name="Error_Join_ect"
            save_dir="/Join_Login/Error_Join_ect.html"
            save_html(HTML_Error_Template(link,block_name,key),save_dir)
            return render(request,"Join_Login/Error_Join_ect.html")
        #계정생성
        else:
            classes=data['classes']
            nickname=data['nickname']
            email= data['useremail']
            password= data['password']
            hint=data['hint']
            gender=data['gender']
            #생성
            url="/login/"
            user_data.objects.create(nickname=nickname,email=email,password=password,hint=hint,gender=gender,classes=classes)
            return render(request,"Join_Login/success_Join.html",{'start_url':start_url,'url':url,'nickname':nickname})    
        #-----------------------------------------------------------------------------#
        
#로그아웃       //html
def logout(request):
    global Global_key
    Global_key['login']=0
    return redirect('/')

#-------------------------------------회원별 개인창--------------------------------------------------------------#
'''
1.html
2.IdeaShare.url 따기 <pk>로
3.대략적인 틀잡기
    -1 로그인하지않은 사람이 방문할때
    -2 로그인
[나중일]
3.이미지 업로드로 꾸미기
4.레이아웃 설계

**** 동시에 다른 ip로 여기 접근하면 html이 새로만들어질텐데 이걸 인식할까?
'''
def blog(request,user_id):
    global Global_key
    user_object=user_data.objects.filter(id=user_id)
    nickname=user_object.values('nickname')[0]['nickname']
    
    image_url="{%static 'images/human.png'%}"
    
    article=f'''
    <div class="container-lg" >
        <div class="row mt-5">
            <div class="col-4 mx-2">
                <div class="card mx-auto my-auto" style="width: 20rem; background-color:#f2f2f2;">
                    <img src="{image_url}" class="card-img-top">
                    <div class="card-body mt-2 me-2">
                    '''
    if Global_key['login']==1:
        bulb=user_object.values('bulb')[0]['bulb']
        coin=user_object.values('coin')[0]['coin']    
        image_bulb_url="{%static 'images/lamp.png'%}"
        image_coin_url="{%static 'images/coin.png'%}"
    
        article+=f'''
                        <p>
                        <img src="{image_bulb_url}" width=30 class='mb-2'> : {bulb}
                        <img src="{image_coin_url}" width=27 class='ml-3 mb-1'> : {coin}
                        </p>
                 '''
    article+=f'''
                        <p class="card-text"><H5>{nickname}</H5></p>
                        <p class="card-text"><a href="www.youtube.com">www.youtube.com</a></p>
                    </div>
                </div>    
            </div>
            '''
    #입력창
    article+=f'''
            <div class="col mx-2" >
                <form method="post" class="post-form" action="dopost">
                    {{% csrf_token %}}
                    <div class="form-floating">
                        <textarea class="form-control" placeholder="Leave a comment here" style="height: 100px" id="comment" required></textarea>
                        <label for="floatingTextarea2">아이디어를 남겨주세요</label>                        
                    </div>
                    <div class="input-group mb-3">
                        <label class="input-group-text" for="inputGroupFile01">Image</label>
                        <input type="file" class="form-control" id="Image">
                    </div>
                    <div class="form-group">
                        <a href="{{start_url}}/dopost/">
                            <button type="submit" class="btn btn-primary mL-auto">게시하기</button>
                        </a>
                    </div>
                </form>    
            </div>    
        
        </div>
    </div>
    '''
    HTML_file=(Title_Template(article))
    save_html(HTML_file,"User/personal.html")    
    
    return render(request,"User/personal.html")

def dopost(request,user_id):
    data=request.POST
    for i in data:
        print(i)
    return render(request,"User/personal.html")

#-------------------------------------카테고리-------------------------------------------------------------------#
'''
나중에하기
'''
def category(request,category_id):
    article=f'''
    
    <div class="container-lg" >
    <H1>category main 창</H1>
    {category_data.objects.filter(id=category_id).values('category_name')[0]['category_name']}
    </div>
    '''
    HTML_file=(Title_Template(article))
    save_html(HTML_file,"Category/subtitle.html")    
        
    return render(request,"Category/subtitle.html")

#-------------------------------------코인 결제------------------------------------------------------------------#
'''
[공부영역]
1. 결제모듈 알아보기
2. 카드로 내 통장에 입금되는지 체크
3. 승인여부를 POST로 받아낼수있는지 체크
https://admin.iamport.kr/
'''
#-------------------------------------개인포스팅-----------------------------------------------------------------#
'''
1. HTML
2. 초반 200자의 짧읜 아이디어 한줄 혹은 이미지파일 업로드 가능케하기 (트위터정도로)
3. 이로인해 bulb가 한개 소모되기

'''

#-------------------------------------카테고리 분류--------------------------------------------------------------#
'''
에타처럼 소비자가 개설할수있게 만들려고하는데
너무 중구난방해질수도있으니 승인후 확장되는식으로 
'''

#-------------------------------------개인-이메일확인 승인--------------------------------------------------------#
'''
1. 이메일 전송하는법 알아보기
2. 이메일내에 링크담아서 보내는법
3. 링크를 눌러 승인햇을때 서버에 어떤게 송신되는지 파악
4. 파악되면 승인 을 True로 전환
https://lar542.github.io/Django/

'''

#-------------------------------------팔로우 구현----------------------------------------------------------------#
'''
1. many-to-many 추가방식을 알아야함
https://himanmengit.github.io/django/2018/02/06/DjangoModels-08-ManyToMany-Self-Symmetrical-Intermediate.html
중개모델 깔아서 다시만들기
https://django-orm-cookbook-ko.readthedocs.io/en/latest/many_to_many.html

'''
#-------------------------------------좋아요 구현----------------------------------------------------------------#
'''
1. 카더라에 의하면 팔로우와 유사함
'''

######차후에 해도될일
#-------------------------------------관리자용 DB 시각화 구현-----------------------------------------------------#


#-------------------------------------기업-승인 시스템 구현------------------------------------------------------#

#-------------------------------------기업용 페이지 구현---------------------------------------------------------#

#-------------------------------------개인-개인 개인-기업 메신저 구현---------------------------------------------#

#-------------------------------------보안 구체화, 디테일유저정보 추가---------------------------------------------#

#------------------------------------ 고객문의 FAQ contact 제작--------------------------------------------------#
'''
1.html
'''






#---------------------------------------------------------------------------------------------------------------#
#-----------------------------------기타 주석용------------------------------------------------------------------#
#준비중         //html
def not_already(request):
    return render(request, "Empty.html")

'''
from django.contrib.auth import views as auth_views

return HttpResponse(HTML_Template(article))
return render(request, "index.html",{'category_list':category,'article':article})
'''