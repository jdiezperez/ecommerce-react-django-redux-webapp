from django.db.models.signals import pre_save

from django.contrib.auth.models import User

def pre_save_user_receiver(sender, instance, *args, **kwargs):
    user = instance
    if user.email != '':
        user.username = user.email

pre_save.connect(pre_save_user_receiver, sender=User)