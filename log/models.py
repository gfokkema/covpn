from django.db import models
from enum import Enum


class LogType(Enum):
    UP = 'up'
    DOWN = 'down'
    IPCHANGE = 'ipchange'
    ROUTE_UP = 'route-up'
    TLS_VERIFY = 'tls-verify'
    AUTH_USER_PASS_VERIFY = 'auth-user-pass-verify'
    CLIENT_CONNECT = 'client-connect'
    CLIENT_DISCONNECT = 'client-disconnect'
    LEARN_ADDRESS = 'learn-address'

    @classmethod
    def list(cls):
        return list(map(lambda c: (c.name, c.value), cls))


class LogEntry(models.Model):
    type = models.CharField(max_length=25, choices=LogType.list())

    def __str__(self):
        return "{0.pk} ({0.type})".format(self)


class LogEntryAttr(models.Model):
    logentry = models.ForeignKey(LogEntry, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    value = models.CharField(max_length=100)

    def __str__(self):
        return "{}: {} = {}".format(self.logentry, self.name, self.value)


def create_log_entry(type, **attr):
    entry = LogEntry(type=type)
    entry.save()
    for k, v in attr.items():
        LogEntryAttr(logentry=entry, name=k, value=v).save()
