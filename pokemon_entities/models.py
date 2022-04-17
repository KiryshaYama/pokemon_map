from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    """Покемон"""
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'
