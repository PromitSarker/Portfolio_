from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('api/projects/', views.ProjectViewSet.as_view({'get': 'list'}), name='api_projects'),
    path('api/blog/', views.BlogPostViewSet.as_view({'get': 'list'}), name='api_blog'),
    path('api/contact/', views.ContactView.as_view(), name='api_contact'),
]