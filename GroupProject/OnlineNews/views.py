# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Author
from models import Category
from models import News
from django.template import loader
import json
from django.core import serializers


# Create your views here.


def index(request):
    response = ""
    template = loader.get_template('index.html')
    context = {
        'data': response
    }
    return HttpResponse(template.render(context, request))


def getAuthors(request):
    auth = Author("1", "1", "", "Dang Minh The", "thekoy.95@gmail.com",
                  "ok ok nothing about him hehe")
    jsonData = json.dumps(auth)
    return HttpResponse(jsonData)


def aboutAuthors(request):
    template = loader.get_template('aboutAuthors.html')
    context = {
        'data': "",
    }
    return HttpResponse(template.render(context, request))

# (self, newsId, title, authorId, cateId, imgUrl, content, description):


def getHottestList(request):
    queryData = list(News.objects.order_by('-Date')[0:16])
    jsonData = serializers.serialize('json', queryData)
    return HttpResponse(jsonData)


def getCategories(request):
    queryData = list(Category.objects.all())
    jsonData = serializers.serialize('json', queryData)
    return HttpResponse(jsonData)
