from django.db import models
from kusskr.apps.blog.models import Article

class Files(models.Model):
    article = models.ForeignKey(Article)
    _file = models.FileField(upload_to='attached_files')
