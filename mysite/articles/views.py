from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse

# Create your views here.
def articles_list(request):
    articles = Articles.objects.all().order_by('date')
    return render(request,'articles/articles_list.html',{'articles':articles})

def articles_details(request,slug):
    return HttpResponse(slug)
    # article = Articles.Objects.get(slug= slug)
    # return render(request,'articles/articles_detail.html',{'article':article})