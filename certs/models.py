from django.db import models
from enum import Enum

import logging


logger = logging.getLogger(__name__)


class CertType(Enum):
    CA = 'ca'
    INTCA = 'intca'
    SERVER = 'server'
    CLIENT = 'client'

    @classmethod
    def list(cls):
        return list(map(lambda c: (c.value, c.name), cls))


class Certificate(models.Model):
    type = models.CharField(max_length=10, choices=CertType.list())
    subject = models.CharField(max_length=25)
    path = models.CharField(max_length=25)

    def save(self, *args, **kwargs):
        created = self.pk is None
        self.path = '?' if created else '/'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.pk} - {self.type}'
