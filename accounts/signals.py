from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Following


@receiver(post_save, sender=User)
def user_create_node(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Following.nodes.get(user_id=instance.id).delete()
        except:
            pass
        follow = Following(name=instance.name, user_id=instance.id).save()