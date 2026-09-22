from django.contrib.auth.models import User
from .models import Notification
from .serializers import UserSerializers, NotificationSerializers
from rest_framework import viewsets
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializers
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.select_related("user").all()
    serializer_class = NotificationSerializers

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ["user"]
    search_fields = ["user", "notifications"]
    ordering_fields = ["created_at"]    