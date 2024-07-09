from django.db import models

class Marca(models.Model):
    descricao = models.CharField(max_length = 50)

    def __str__ (self):
        return f"{self.descricao} {(self.id)}"