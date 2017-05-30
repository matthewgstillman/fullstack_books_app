from __future__ import unicode_literals

from django.db import models

class BookManager(models.Manager):
    def title_must_not_be_blank(self, postData):
        errors = []
        if postData['title'] =="":
            errors.append("title must not be blank!")
        if postData['author'] =="":
            errors.append("author must not be blank!")
        if postData['category'] =="":
            errors.append("category must not be blank!")
            print errors
        if len(errors) == 0:
            b = Book.objects.create(title=postData['title'], author=postData['author'])
            return [True, b]
        else:
            return [False, False]

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()
# Create your models here.
    def __unicode__(self):
        return "title: " + self.title + " author: " + self.author + " category: " + self.category
