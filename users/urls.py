from rest_framework.routers import DefaultRouter

from users import views

router = DefaultRouter()
router.register(r'api/v1/users', views.UserViewSet)
urlpatterns = router.urls
