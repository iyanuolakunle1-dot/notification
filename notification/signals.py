from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Notification


@receiver(
    post_save,
    sender=Notification
)
def notification_created(
    sender,
    instance,
    created,
    **kwargs
):

    if not created:
        return

    channel_layer = get_channel_layer()

    async_to_sync(
        channel_layer.group_send
    )(
        "notifications",
        {
            "type": "notification_message",
            "message": instance.message,
        }
    )