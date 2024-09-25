from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=255)
    price = models.FloatField()
    about = models.TextField()
    discount = models.IntegerField()
    count = models.IntegerField()
    oyiga_t = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    @property
    def is_sale(self):
        return self.price - (self.price * self.discount / 100)


class Meta:
    ordering = ['-id']



