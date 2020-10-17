from django.db import models
from django.contrib.auth.models import Group


class Config(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    option = models.CharField(max_length=20)
    value = models.CharField(max_length=100)

    def __str__(self):
        return "{0.option} {0.value}".format(self)


class Route(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    mask = models.GenericIPAddressField()
    gateway = models.GenericIPAddressField(blank=True, null=True)
    metric = models.IntegerField(blank=True, default=0)

    def __str__(self):
        params = filter(None, [self.gateway, self.metric])
        return ' '.join(['route {0.ip} {0.mask}'.format(self), *params])
