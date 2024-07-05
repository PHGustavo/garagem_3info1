from django.db import models

class Acessorio(models.Model):
    descricao = models.CharField(max_length = 100)

    def _str_ (self):
        return f"{self.descricao} {(self.id)}"
class Meta:
    verbose_name = "Acessorio"
    verbose_name_plural = "Acessorios"