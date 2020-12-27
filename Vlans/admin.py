from django.contrib import admin
from .models import Vlan, IPaddress

# Register your models here.

class IPaddressAdmin(admin.ModelAdmin):
    list_display = ('ipaddress', 'description', 'used', 'vlan')
    readonly_fields = ('ipaddress','vlan')
    list_filter = ('vlan', )

class VlanAdmin(admin.ModelAdmin):
    list_display = ('number', 'description')

admin.site.register(Vlan, VlanAdmin)
admin.site.register(IPaddress, IPaddressAdmin)

