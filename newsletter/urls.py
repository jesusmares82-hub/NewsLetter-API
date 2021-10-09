"""newsletter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_swagger.views import get_swagger_view

from users.views import UserViewSet

schema_view = get_swagger_view(title='Pastebin API')

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include(router.urls)),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('', include(r'users.urls')),
                  path('', include(r'newsletters.urls')),
                  path('', include(r'votes.urls')),
                  path('', include(r'tags.urls')),
                  url(r'^$', schema_view)

              ] + router.urls
