from django.db import models

from django.db.models.fields import related



class user_data(models.Model):
    '''
    nickname: 활동 닉네임
    email: e-mail
    password: PW
    hink : PW 힌트
    gender: 성별
    follower: 위계정을 팔로워들 닉네임
    following: 위계정이 팔로잉하는 닉네임
    classes: 등급
    Admin_Approval: 관리자 승인(기업이나 관리자 가입시)
    bulb: 게시코인
    coin: 캐쉬코인
    '''
    Classes_choice=[
        ('P','Personal'),   #개인
        ('C','Company'),    #기업
        ('A','Admin'),      #관리자
        ('H','High_Admin'), #상위관리자
    ]
    Gender_choice=[
        ('M','Male'),
        ('F','Female'),
    ]
    nickname=models.CharField(max_length=10,unique=True)
    email= models.EmailField(unique=True)
    password= models.CharField(max_length=20)
    hint=models.CharField(max_length=20,default='')
    gender=models.CharField(blank=True,max_length=20,choices=Gender_choice)

    follower=models.ManyToManyField("self",default="")
    following=models.ManyToManyField("self",default="")
    
    classes=models.CharField(blank=True,max_length=20,choices=Classes_choice, default='P')
    Admin_Approval=models.BooleanField(default=False)

    bulb=models.PositiveIntegerField(default=5)
    coin=models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.nickname

class category_data(models.Model):
    '''
    catagory_name:목차 데이터
    '''
    category_name= models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.category_name

class Time_stamp(models.Model):
    '''
    create_at: 생성날짜
    updated_at: 수정날짜
    '''
    create_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

#class blog_data():
#    def __str__(self):
#        return 0


class post_data(Time_stamp):
    '''
    nickname: 작성 닉네임
    category_name: 해당포스트의 목차
    
    image: 이미지 게시
    post_data_short: 초안 게시글 데이터

    thumb_cost: 좋아요수
    approval: 일정 수이상 좋아요 받을시 True값 표시
    
    post_data_long: 위값이 트루일때 사용가능한 더 큰 게시데이터
    '''
    nickname=models.ForeignKey(user_data, on_delete=models.CASCADE)
    category_name= models.ForeignKey(category_data ,on_delete=models.CASCADE)
    
    image=models.ImageField(blank=True)
    post_data_short=models.CharField(max_length=200)
    
    thumb_cost=models.PositiveIntegerField(default=0)
    long_approval=models.BooleanField(default=False)

    post_data_long=models.TextField()
    
    def __str__(self):
        return self.post_data_short

class Reply(Time_stamp):
    '''
    reply: reply->post_data 연결관계
    comment: 댓글내용
    '''
    nickname=models.ForeignKey(user_data, on_delete=models.CASCADE)
    post = models.ForeignKey(post_data, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.comment
