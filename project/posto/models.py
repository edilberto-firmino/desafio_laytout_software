from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models

class Tanques (models.Model):
    conteudo=models.CharField(max_length=15)
    volume_m3=models.DecimalField(max_digits=12, decimal_places=6)
    def __str__(self):
        return self.conteudo

class Bombas (models.Model):
    referencia=models.CharField(max_length=50)
    tanque=models.ForeignKey(Tanques, on_delete=models.CASCADE)
    def __str__(self):
        return self.referencia

class Vendas (models.Model):
    created_at=models.DateTimeField(default=timezone.now(), editable=False)
    litros=models.DecimalField(max_digits=12, decimal_places=6)
    valor_abastecido=models.DecimalField(max_digits=12, decimal_places=6)
    valor_de_imposto=models.DecimalField(max_digits=12, decimal_places=6)
    bomba=models.ForeignKey(Bombas, on_delete=models.CASCADE)
    

@receiver(post_save, sender=Vendas)   
def calcular_imposto(sender, instance, created, **kwargs):
    def imposto(val):
        return (val*13)/100
        
    if created:
        (
            Vendas
            .objects
            .filter(pk=instance.pk)
            .update(valor_de_imposto=imposto(instance.valor_abastecido))
        )



