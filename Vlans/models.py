from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse

class Vlan(models.Model):
    number      =   models.SmallIntegerField(unique=True, blank=False, null=False, primary_key=True)
    description =   models.TextField(max_length=150, blank=True)
    network     =   models.CharField(max_length=150, blank=True)
    date        =   models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['number',]

    def __str__(self):
        return "Vlan"+str(self.number)

    def get_absolute_url(self):
        return reverse('vlans:vlan_detail', kwargs={'pk':self.number})


class IPaddressManager(models.Manager):
    def get_queryset(self):
        qs = super(IPaddressManager, self).get_queryset()
        qsorted = sorted(qs, key = lambda item: [int(octet) for octet in item.ipaddress.split(".")])
        print(type(qsorted[0])) #list not queryset
        return qs
        #return qs.annotate('a','b','c','d' = 'ipaddress'.split('.')).order_by('a','b','c','d')

class IPaddress(models.Model):
    ipaddress   = models.GenericIPAddressField(unique=True, protocol="IPv4")
    description = models.CharField(max_length=150, blank=True, null=True)
    used        = models.BooleanField(default=False)
    vlan        = models.ForeignKey(Vlan, on_delete = models.CASCADE)
    #objects = IPaddressManager()

    def __str__(self):
        return self.ipaddress
    
    class Meta:
        verbose_name = 'IPaddress'
        verbose_name_plural = 'IPaddresses'
        ordering = ['id']


