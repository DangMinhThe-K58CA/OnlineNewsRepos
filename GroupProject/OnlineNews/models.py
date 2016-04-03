from __future__ import unicode_literals

from django.db import models
from datetime import date
# Create your models here


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100, unique=True)
    AboutAuthor = models.CharField(max_length=200)
    Date = models.DateField(default=date.today)


class News(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    CateId = models.CharField(max_length=100)
    ImgUrl = models.CharField(max_length=200)
    Content = models.CharField(max_length=5000)
    Description = models.CharField(max_length=200)
    Date = models.DateField(default=date.today)
    # other menthod here !
    # please not change attributes in all classes.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Date = models.DateField(default=date.today)
    # other menthod here !
    # please not change attributes in all classes.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100, unique=True)
    Password = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    Date = models.DateField(default=date.today)


class Viewer(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    About = models.CharField(max_length=200)
    Address = Address = models.CharField(max_length=200)
    Phone = models.CharField(max_length=50)
    Feeling = models.CharField(max_length=100)
    Date = models.DateField(default=date.today)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    NewsId = models.ForeignKey(News, on_delete=models.CASCADE)
    ViewerId = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    Content = models.CharField(max_length=5000)
    Date = models.DateField(default=date.today)


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    NewsId = models.ForeignKey(News, on_delete=models.CASCADE)
    ViewerId = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    Date = models.DateField(default=date.today)
