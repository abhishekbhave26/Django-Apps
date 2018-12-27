from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts=[
	{
		'name':'Aaron Ramsey',
		'title':'Ramsey to leave Arsenal on free',
		'content':'Arsenal star Aaron Ramsey set to join PSG in a January move for about 10-15 million pounds'

	},
	{
		'name':'Chris Smalling',
		'title':'Chris Smalling signs new contact',
		'content':'Utd star sign new 150k pounds per week deal under new coach'

	}

]

def home(request):
    
    context={'posts':posts}
    return render(request,'news/home.html',context)


def about(request):
    return render(request,'news/about.html',{'title':'About'})
    