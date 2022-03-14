from django.http import HttpResponse

def about(request):
    return HttpResponse('This is my first page')


def home(request):
    return HttpResponse('This is my home')