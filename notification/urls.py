from .views import UserViewSet, NotificationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"notifications", NotificationViewSet, basename="notifications")


urlpatterns=router.urls