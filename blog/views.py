from django.shortcuts import render
from .models import Link,Feedback,Articles

# Create your views here.

def index(request):

    miles = Link.objects.all()

    return render (request,'index.html',{'miles': miles})

def contact(request):
    if request.method == 'POST':
        username = request.POST['username']
        useremail = request.POST['useremail']
        subject = request.POST['subject']
        message = request.POST['message']

        feedback= Feedback(username=username,useremail=useremail,subject=subject,message=message)

        feedback.save()
        

        return render (request,'contact.html',{})

    else:
        return render (request,'contact.html',{'contact': contact})


def blog(request):

    blogs = Articles.objects.all()

    return render (request,'blog.html',{'blogs': blogs})

def single_blog(request):

    s_blogs = Articles.objects.all()


    return render (request,'single_blog.html',{'s_blogs': s_blogs})

    
