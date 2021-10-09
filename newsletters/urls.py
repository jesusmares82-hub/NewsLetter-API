from rest_framework.routers import DefaultRouter

from newsletters import views

router = DefaultRouter()
router.register(r'api/v1/newsletters', views.NewsViewSet)
urlpatterns = router.urls
