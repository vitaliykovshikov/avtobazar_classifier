#encoding: utf-8
from django.conf.urls import patterns, url

from classifier import views

urlpatterns = patterns('',
    url(r'^(?P<make>[a-zA-Z0-9_.-]+)\+(?P<model>[a-zA-Z0-9_.-]+)/(?P<year_from>d+)/(?P<type>[a-zA-Z]+)/$',
        views.ModelYearPage.as_view(), name='model_year_page'),

    url(r'^(?P<make>[a-zA-Z0-9_.-]+)/(?P<type>[a-zA-Z]+)/$',
        views.MakePage.as_view(), name='make_page'),

    url(r'^(?P<make>[a-zA-Z0-9_.-]+)\+(?P<model>[a-zA-Z0-9_.-]+)/(?P<type>[a-zA-Z]+)/$',
        views.ModelPage.as_view(), name='model_page'),

    url(r'^(?P<make>[a-zA-Z0-9_.-]+)\+(?P<model>[a-zA-Z0-9_.-]+)\+(?P<modification>[a-zA-Z0-9_.-]+)/(?P<type>[a-zA-Z]+)/$',
        views.ModificationPage.as_view(), name='modification_page'),
)
