from django.db import models

# Create your models here.

class Estudios(models.Model):

    data_preencimento = models.DateField(null=True)
    nome = models.CharField(max_length = 200)
    pais = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self):
        return self.nome