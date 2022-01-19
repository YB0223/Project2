from django.urls import path,include

from . import views
from django.contrib.auth import views as auth_views

app_name='IdeaShare'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login, name='login'),
    path('login/dologin',views.dologin,name='dologin'),
    path('logout/',views.logout, name='logout'),
    path('Join/',views.join_site, name='Join'),
    path('Join/doJoin',views.doJoin, name='doJoin'),

    #not already
    path('blog/<user_id>/',views.blog, name='blog'),
    path('blog/<user_id>/dopost',views.dopost, name='post'),
    path('category/<category_id>/',views.category,name='category'),
    
    path('service/FAQ/',views.not_already, name='FAQ'),
    path('service/GG/',views.not_already, name='GG'),
    path('service/seh/',views.not_already, name='gg'),
    path('Contact/',views.not_already, name='Contact'),
    

]