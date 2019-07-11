
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


{'posts':Post.objects.all()}


# Create your views here.


def home(request):	
	context={'posts': Post.objects.all()}									
	return render(request, 'blog/home.html',context) 

# def home(request):							#home calls posts
#  	context={'posts': posts}				#then returns content when calling  file inside blog called 'home.html (inside templates folder) --> html code for first blog post iin home page'
#  	return HttpResponse('<h1> Blog Home </h1>', {'title': 'About'})
def about(request):	
								
	return render(request, 'blog/about.html') 

# def about(request):
# 	return HttpResponse('<h1> Blog About </h1>', {'title': 'About'}) #HTML code to create a header 
def information(request):
	return render(request, 'blog/information.html')

def author(request):
	return render(request,'blog/author.html')
