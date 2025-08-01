from django.db import models

class Tovar(models.Model):
    name_prep = models.CharField(max_length=255)
    ean13 = models.CharField(max_length=255)

    def __str__(self):
        return self.name_prep


class ClientTovar(models.Model):
    name_prep = models.CharField(max_length=255)
    ean13 = models.CharField(max_length=255)

    def __str__(self):
        return self.name_prep


class MatchedTovar(models.Model):
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    client_tovars = models.ManyToManyField(ClientTovar)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tovar.name_prep} - {self.quantity}"
