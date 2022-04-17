from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    """Покемон"""
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return f'{self.title}'

class PokemonEntity(models.Model):
    """Координаты покемона"""
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    appeared_at = models.DateTimeField(
        null=True,
        blank=True)
    disappeared_at = models.DateTimeField(
        null=True,
        blank=True)
    level = models.IntegerField()
    health = models.IntegerField()
    strength = models.IntegerField()
    defence = models.IntegerField()
    stamina = models.IntegerField()