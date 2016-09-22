# -*- coding:utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8') 

from django.db import models
from django.contrib.auth.models import AbstractUser
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse

# Create your models here.
#用户模型
class User(AbstractUser):

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username

#分类模型
class Category(models.Model):
    name = models.CharField(max_length=30)
    index = models.IntegerField('显示顺序(从小到大)',default=999)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['index','id']

    def __unicode__(self):
        return self.name

#文章模型
class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name='文章标题')
    description = models.CharField(max_length=200,verbose_name='文章描述')
    content = UEditorField(default=u'',height=300,width=1000,imagePath='uploads/images/',toolbars='besttome',filePath='upload/files/',verbose_name='文章内容')
    publish_date = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    recommend = models.BooleanField(default=False,verbose_name='是否推荐')
    click_count = models.IntegerField(default=0,verbose_name='点击次数')
    user = models.ForeignKey(User,verbose_name='作者')
    category = models.ForeignKey(Category,blank=True,null=True,verbose_name='文章分类')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-publish_date']

    def __unicode__(self):
        return self.title

#评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    user = models.ForeignKey(User,blank=True,null=True,verbose_name='用户')
    publish_date = models.DateTimeField(auto_now_add=True,verbose_name='评论时间')
    article = models.ForeignKey(Article,blank=True,null=True,verbose_name='文章')
    father = models.ForeignKey('self',blank=True,null=True,verbose_name='父级评论')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.id)

#友情链接模型
class Links(models.Model):
    name = models.CharField(max_length=50,verbose_name='标题')
    url = models.URLField(verbose_name='url地址')
    description = models.CharField(max_length=200,verbose_name='描述')
    publish_date = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    index = models.IntegerField(default = 999,verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

#广告模型
class Ad(models.Model):
    title = models.CharField(max_length=50,verbose_name='广告标题')
    description = models.CharField(max_length=200,verbose_name='广告描述')
    description2 = models.CharField(blank=True,null=True,max_length=200,verbose_name='广告标题2')
    image_url = models.ImageField(upload_to='ad/%Y/%m',verbose_name='图片路径')
    url = models.URLField(blank=True,null=True,verbose_name='链接url')
    publish_date = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    index = models.IntegerField(default=999,verbose_name='排列顺序(从小到大)')
    adtype_choice = ((1,'顶部广告'),(2,'右上广告'),(3,'右下广告'))
    adtype = models.IntegerField(default=1,choices=adtype_choice,verbose_name='广告位置')


    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name
        ordering = ['index','id']

    def __unicode__(self):
        return self.title