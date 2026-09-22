from .models import Notification
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ["id", "username", "email", "password"]


class NotificationSerializers(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
    source="user",
    queryset=User.objects.all(),
    write_only=True,
)
    class Meta:
        model = Notification
        fields = ["id", "user", "user_id", "message", "is_read", "created_at"]