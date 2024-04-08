from shop.tasks import send_email
from django.dispatch import receiver, Signal
from django.db.models.signals import post_save
from django_rest_passwordreset.signals import reset_password_token_created
from users.models import ConfirmEmailToken, User

new_order = Signal()

@receiver(new_order)
def new_order_signal(sender, user_id, **kwargs):
    """
    Отправляем письмо при изменении статуса заказа
    """
    try:
        user = User.objects.get(id=user_id)
        send_email.delay("Обновление статуса заказа", "Заказ сформирован", [user.email])
    except User.DoesNotExist:
        print(f"User with id {user_id} does not exist.")
