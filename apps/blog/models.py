from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from kusskr.apps.files.models import Files

class Article(models.Model):
    writer = models.ForeignKey(_('writer'), User)
    written_datetime = models.DateTimeField(_('written_datetime'), auto_now=True)
    subject = models.CharField(_('subject'), max_length=100)
    content = models.TextField(_('content')) 
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.subject

class Comment(models.Model):
    nickname = models.CharField(max_length=10)
    content = models.TextField()
    password = models.CharField(max_length=100) 
    article = models.ForeignKey(Article)

class Category(models.Model): 
    name = models.TextField()
    parent = models.ForeignKey(Category)

