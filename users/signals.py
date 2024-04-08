from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django_rest_passwordreset.signals import reset_password_token_created
from users.models import ConfirmEmailToken, User
from celery import shared_task

new_user_registered = Signal()


@shared_task
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, **kwargs):
    """
    Отправляем письмо с токеном для сброса пароля
    """
    msg = EmailMultiAlternatives(
        f"Password Reset Token for {reset_password_token.user}",
        reset_password_token.key,
        settings.EMAIL_HOST_USER,
        [reset_password_token.user.email]
    )
    msg.send()


@shared_task
@receiver(post_save, sender=User)
def new_user_registered_signal(sender, instance, created, **kwargs):
    """
    Отправляем письмо с токеном для подтверждения
    """
    if created and not instance.is_active:
        token, _ = ConfirmEmailToken.objects.get_or_create(user_id=instance.pk)

        msg = EmailMultiAlternatives(
            f"Password Reset Token for {instance.email}",
            token.key,
            settings.EMAIL_HOST_USER,
            [instance.email]
        )
        msg.send()
