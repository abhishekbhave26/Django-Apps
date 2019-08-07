from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

posts=[
	{
		'author':'David Ornstein',
		'title':'Ramsey to leave Arsenal on free',
		'content':'Arsenal star Aaron Ramsey set to join PSG in a January move for about 10-15 million pounds',
		'date_posted':'12/20/2018'

	},
	{
		'author':'Guilleme Balague',
		'title':'Chris Smalling signs new contact',
		'content':'Utd star sign new 150k pounds per week deal under new coach',
		'date_posted':'12/15/2018'

	}

]

def home(request):
    
    context={'posts':Post.objects.all()}
    return render(request,'news/home.html',context)


def about(request):
    return render(request,'news/about.html',{'title':'About'})
    