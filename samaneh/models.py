from django.db import models


# Create your models here.
class Work(models.Model):
    name = models.CharField(max_length=255, default='unknown work')
    price = models.IntegerField(default=0)
    estimate = models.IntegerField(verbose_name='days', default=99)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, default=None)
    description = models.TextField(default='')
    created = models.DateTimeField(auto_now=True)

