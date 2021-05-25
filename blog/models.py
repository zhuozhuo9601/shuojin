from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Leaderboard(models.Model):
    "分数表"
    name = models.CharField('客户端名称', max_length=200, unique=True)
    fraction = models.IntegerField(verbose_name='分数', default=0,
                                validators=[MaxValueValidator(10000000), MinValueValidator(1)])


    class Meta:
        verbose_name = '排行榜'
        verbose_name_plural = '排行榜'
        unique_together = (("fraction",),)

    def __str__(self):
        return self.name

