from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Config(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    option = models.CharField(max_length=20)
    value = models.CharField(max_length=100)

    def __str__(self):
        return "({}) \"{} {}\"".format(self.group, self.option, self.value)


class Route(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    mask = models.GenericIPAddressField()
    gateway = models.GenericIPAddressField(blank=True, null=True)
    metric = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return "({}) \"{}/{}\"".format(self.group, self.ip, self.mask)
