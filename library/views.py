from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.


class BookList(TemplateView):
    template_name= "index.html"
    def book_list(self, request, *args, **kwargs):
        