from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Project, BlogPost, ContactMessage
from .serializers import ProjectSerializer, BlogPostSerializer, ContactMessageSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class ContactView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'})
        return Response(serializer.errors, status=400)

def home(request):
    projects = Project.objects.all()
    blog_posts = BlogPost.objects.all()
    return render(request, 'index.html', {
        'projects': projects,
        'blog_posts': blog_posts
    })

