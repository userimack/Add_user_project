from django.shortcuts import render

# Create your views here.

def createuser(request):
	return render(request, 'createuser.html',{})
