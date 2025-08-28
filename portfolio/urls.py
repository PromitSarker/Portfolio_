from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ProjectViewSet, BlogPostViewSet, ContactView
from core import views
from django.conf import settings
from django.conf.urls.static import static



# API routes
router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('blog', BlogPostViewSet)
  # simpler URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/contact/', ContactView.as_view(), name='contact'),
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
