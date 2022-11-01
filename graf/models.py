from django.db import models
from colorfield.fields import ColorField

class Test(models.Model):
    jmeno_objektu = models.CharField(max_length=200)
    pocet_objektu = models.IntegerField()
    color = ColorField(default='#000000')
    borderColor = ColorField(default='#FF00FF')

    def __str__(self):
        return "{} - {}".format(self.jmeno_objektu, self.pocet_objektu, self.color, self.borderColor)
