from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('This is main page!!!')


def group_posts(request, slug):
    return HttpResponse(f'There is group posts: {slug}')
