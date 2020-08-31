from django.http import HttpResponse
from django.shortcuts import render, redirect


def home_view(request):
    return redirect('posts:main-post-view')

    # return HttpResponse('Hello world')
