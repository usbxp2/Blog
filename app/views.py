# -*- coding:utf-8 -*-
from django.shortcuts import render,redirect
from app.models import *
from django.conf import settings
#用户登录，注销，验证
from django.contrib.auth import logout,login,authenticate
#django内置的分页器
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
#django日志管理器
import logging
#密码写入数据库是加密
from django.contrib.auth.hashers import make_password
#导入forms表单
from forms import *


# Create your views here.

#设置从哪个应用获取log
logger = logging.getLogger('app.views')

#全局
def global_setting(request):
    SITE_NAME = settings.SITE_NAME
    #分类信息（导航数据）
    nav_list = Category.objects.all()
    #友情链接信息
    link_list = Links.objects.all()
    #广告信息
    ad_list = Ad.objects.filter(adtype=1)
    ad_frist = Ad.objects.get(index=1)
    ad_right_top = Ad.objects.filter(adtype=2)
    ad_right_under = Ad.objects.filter(adtype=3)
    #最新文章信息
    article_list_latest = Article.objects.all()[:6]
    #热门文章信息
    article_list_hot = Article.objects.order_by('-click_count')[:6]

    return locals()

#分页代码
def getPage(request,article_list):
    #设置每页显示的数量
    paginator = Paginator(article_list,8)
    try:
        #获取跳转的页，如果没有，则默认为1
        page = int(request.GET.get('page',1))
        article_list = paginator.page(page)
    except (EmptyPage,InvalidPage,PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list


#首页
def index(request):
    try:
        article_list = getPage(request,Article.objects.all())
    except Exception as e:
        logger.error(e)

    return render(request,'index.html',locals())

#文章内容页
def content(request):
    #获取文章id
    id = request.GET.get('id',None)  #没获取到则默认为None
    try:
        article = Article.objects.get(pk=id)
        #文章浏览量统计，每访问一次+1
        article.click_count = article.click_count + 1
        article.save()
        #获取外键表中的id字段。即获取文章分类id
        category_id = article.category.id
        comment_list = Comment.objects.filter(article=article.id)
        user_list = []
        user_count = 0
        for i in comment_list:
            if i.user not in user_list:
                user_list.append(i.user)
                user_count += 1
    except Article.DoesNotExist:
        return render(request,'fails.html',{'reason':'没有找到对应的文章'})

    return render(request,'content.html',locals())


#文章分类，分类下的所有文章
def box(request):
    #获取分类id
    id = request.GET.get('id',None)
    try:
       #过滤出category字段值等于id的数据，category为外键
       article_list = Article.objects.filter(category=id)
       article_list = getPage(request,article_list)
    except Exception as e:
       logger.error(e)

    return render(request,'index.html',locals())

def comment_post(request):
    if request.method == 'POST':
        comment_content = request.POST.get('fabiao_name')
        article_id = request.POST.get('content_id')
        if comment_content is not None:
            comment = Comment.objects.create(content=comment_content,user=request.user,article_id=article_id)
            comment.save()
        else:
            return render(request,'fails.html',{'reason': '请添加评论内容'})
    return redirect(request.META['HTTP_REFERER'])



def reg(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                #注册
                user = User.objects.create(username=reg_form.cleaned_data["username"],
                                           password=make_password(reg_form.cleaned_data['password']),)
                user.save()

                #登录
                #指定默认的登录验证方式
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request,user)
                return redirect(request.POST.get('source_url'))
            else:
                return render(request,'failure.html',{'reason':reg_form.errors})
        else:
            reg_form = RegForm()
    except Exception as e:
        logger.error(e)
    return render(request,'reg.html',locals())

def do_login(request):
    try:
        if request.method == 'POST':
            #实例化form
            login_form = LoginForm(request.POST)
            #如果login_form是有效的
            if login_form.is_valid():
                #从form获取数据
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(username=username,password=password)
                if user is not None:
                    #指定默认的登录验证方式
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    #登录
                    login(request,user)
                else:
                    return render(request,'login.html',{'reason':'登录验证失败','login_form':login_form})
                #登录成功，返回登录前页面
                return redirect(request.POST.get('source_url'))
            else:
                return render(request,'login.html',{'reason':'输入内容无效','login_form':login_form})
        else:
            #返回登录框
            login_form = LoginForm()
    except Exception as e:
        logger.error(e)
    return render(request,'login.html',locals())

def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        logger.error(e)
    return redirect(request.META['HTTP_REFERER'])

