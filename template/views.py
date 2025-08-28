from django.shortcuts import render

def index(request):
    return render(request, 'template/index.html')  # Note the template/index.html path
