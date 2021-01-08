from django.db import models

# Create your models here.
my_choices = (
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL')
)


class selldata(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    size = models.CharField(max_length=10, choices=my_choices)
    disc = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
