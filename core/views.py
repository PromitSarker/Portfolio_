from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics
from .models import Project, BlogPost, ContactMessage
from .serializers import ProjectSerializer, BlogPostSerializer, ContactMessageSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class ContactView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer


from django.shortcuts import render
from .models import Project, BlogPost

def home(request):
    # If you want, you can pass real data instead of JS mock
    projects = Project.objects.all()
    blog_posts = BlogPost.objects.all()
    return render(request, 'index.html', {
        'projects': projects,
        'blog_posts': blog_posts
    })

