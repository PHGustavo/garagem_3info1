from django.db import models
from .marca import marca
from .categoria import categoria

class Modelo(models.Model):
    descricao = models.CharField(max_length = 100)

    marca = models.ForeignKey(
        marca, on_delete=models.PROTECT, related_name="veiculos", null=True, blank=True
    )

    categoria = models.ForeignKey(categoria, on_delete=models.PROTECT, related_name="veiculos", null=True, blank=True)
    
    def __str__ (self):
        return f"{self.descricao} {(self.id)}"
    