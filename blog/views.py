from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost



# Create your views here.

def archive(request):
	posts = BlogPost.objects.all()
	mi_template = loader.get_template('archive.html')
	mi_contexto = Context({'posts':posts})
	return HttpResponse(mi_template.render(mi_contexto))

