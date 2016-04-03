from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^aboutAuthors', views.aboutAuthors, name='profile'),
    url(r'^getAuthors', views.getAuthors, name='getAuthors'),
    url(r'^getCategories', views.getCategories, name='getCategories'),
    url(r'^getHottestList', views.getHottestList, name='getHottestList'),
]
urlpatterns += staticfiles_urlpatterns()
