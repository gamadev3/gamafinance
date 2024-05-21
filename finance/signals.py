from django.db.models.signals import post_save
from django.dispatch import receiver
from finance.models import Conta
from services.notify import Notify


@receiver(post_save, sender=Conta)
def send_notification_when_pay(sender, instance, **kwargs):
    notify = Notify()
    data = {
        "nome": instance.nome,
        "valor": str(instance.valor),
        "situacao": "PAGO"
    }
    notify.send_event(data)

