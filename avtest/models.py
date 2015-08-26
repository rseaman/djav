from django.db import models


class User(models.Model):
    alienvaultid = models.CharField(max_length=12)

    def __unicode__(self):
        return '{"alienvaultid": "%s"}' % (self.alienvaultid)


class Visit(models.Model):
    user      = models.ForeignKey(User)
    address   = models.CharField(max_length=15)
    timestamp = models.CharField(max_length=10)
    endpoint  = models.CharField(max_length=128)

    def __unicode__(self):
        return '{"address": "%s", "timestamp": "%s", "endpoint": "%s"}' % (self.address,
                                                                           self.timestamp,
                                                                           self.endpoint)