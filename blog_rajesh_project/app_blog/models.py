from django.db import models
from django.contrib.auth.models import User  #use in author field
from django.urls import reverse # import to urls.py
from django.utils import timezone
# Create your models here.

from taggit.managers import TaggableManager #taggit

class CustomManager(models.Manager):   #custom manager should be child of model to mange
    def get_queryset(self):         #one method is  call
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=260,unique_for_date='publish')
    author=models.ForeignKey(User, related_name='blog_posts',on_delete=models.PROTECT)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=100,choices=STATUS_CHOICES ,default='draft')
    objects=CustomManager() #when you should be call qs then only u have to display publish post is call custom manager
    # tag is manage to all post
    tags=TaggableManager() #tag is manage to all post
    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

#Model related to comments sections

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.PROTECT)
    name=models.CharField(max_length=110)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=('-created',)
    def __str__(self):
        return "Commented By {} on {}".format(self.name,self.post)



