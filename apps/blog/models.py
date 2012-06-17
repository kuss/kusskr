# -*- coding: utf-8
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    user = models.ForeignKey(User)
    
    # Settings
    number_of_articles_per_page = models.PositiveSmallIntegerField(default=10)

class Category(models.Model): 
    name = models.TextField()
    parent = models.ForeignKey('self')

class Article(models.Model):
    writer = models.ForeignKey(User)
    written_datetime = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=100)
    content = models.TextField() 
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.subject

class Comment(models.Model):
    nickname = models.CharField(max_length=10)
    content = models.TextField()
    password = models.CharField(max_length=100) 
    article = models.ForeignKey(Article)


