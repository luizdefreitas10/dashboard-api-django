# from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models.register import UserRegistrationLog
# from .models.user import User


# @receiver(post_save, sender=get_user_model())
# def log_user_creation(sender, instance, created, **kwargs):
    
#     if created:
#         UserRegistrationLog.objects.create(
#             created_by=instance,
#             created_user=instance
#         )