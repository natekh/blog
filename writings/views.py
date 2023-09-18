from django.shortcuts import render

def index(request):
    context = {'message': 'hello world'}
    return render(request, 'index.html', context=context)




