from django.db import models


class Auto(models.Model):
    firm = models.CharField(max_length=100,verbose_name='Марка')
    model = models.CharField(max_length=100, verbose_name='Модель')
    color = models.CharField(max_length=50,verbose_name='Цвет')
    volume = models.FloatField(verbose_name='Обьём')
    engine = models.ForeignKey('Engine',verbose_name='Двигатель', on_delete=models.CASCADE)
    transmission = models.ForeignKey('Transmission',verbose_name='Трансмиссия', on_delete=models.CASCADE)
    price = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Автомобили'
        verbose_name = 'Автомобиль'
        ordering = ['-price']


class Engine(models.Model):
    name = models.CharField(max_length=50,verbose_name='Тип двигателя')

    class Meta:
        verbose_name_plural = 'Двигатели'
        verbose_name = 'Двигатель'

    def __str__(self):
        return self.name

class Transmission(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тип трансмиссии')

    class Meta:
        verbose_name_plural = 'Трансмиссии'
        verbose_name = 'Трансмиссия'

    def __str__(self):
        return self.name

# Create your models here.
