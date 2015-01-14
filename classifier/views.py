#encoding: utf-8
from django.shortcuts import render
from django.views.generic import TemplateView

class MakePage(TemplateView):
    template_name = 'classifier/make_page.html'

class ModelPage(TemplateView):
    template_name = 'classifier/model_page.html'

class ModelYearPage(TemplateView):
    template_name = 'classifier/model_year_page.html'

class ModificationPage(TemplateView):
    template_name = 'classifier/modification_page.html'
