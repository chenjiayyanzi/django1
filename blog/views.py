from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Jiayu chen',
        'title': 'First blog',
        'content': 'this is the first blog',
        'post_date': 'August 28 2019'
    },
    {
        'author': 'Clem Cherrey',
        'title': 'Second blog',
        'content': 'this is the second blog',
        'post_date': 'August 29 2019'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts1': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
