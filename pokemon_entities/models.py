from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    """Покемон"""
    id = models.AutoField(auto_created=True, primary_key=True)
    title_ru = models.CharField(max_length=200, verbose_name='Русское название')
    title_en = models.CharField(max_length=200, null=True, blank=True, verbose_name='Английское название')
    title_jp = models.CharField(max_length=200, null=True, blank=True, verbose_name='Японское название')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Из кого эволюционирует')


    def __str__(self):
        return f'{self.title_ru}'

class PokemonEntity(models.Model):
    """Координаты покемона"""
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='Покемон')
    lat = models.FloatField(null=True, verbose_name='Широта')
    lon = models.FloatField(null=True, verbose_name='Долгота')
    appeared_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Время появления')
    disappeared_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Время исчезновения')
    level = models.IntegerField(verbose_name='Уровень')
    health = models.IntegerField(verbose_name='Здоровье')
    strength = models.IntegerField(verbose_name='Сила')
    defence = models.IntegerField(verbose_name='Защита')
    stamina = models.IntegerField(verbose_name='Выносливость')

    def __str__(self):
        return f'{self.pokemon.title_ru} {self.level} уровня'