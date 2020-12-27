import os
import ipaddress
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IPaddManagement.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from Vlans.models import IPaddress, Vlan

ips = [str(ip) for ip in ipaddress.ip_network(sys.argv[1]).hosts()]
print(type(ips[0]))

vlan1 = Vlan.objects.get_or_create(number=int(sys.argv[2]), network=sys.argv[1])[0]
print(type(vlan1))
objectlist = []
for ip in ips:
    ip1 = IPaddress(ipaddress=ip,vlan=vlan1)
    objectlist.append(ip1)

print(objectlist)
print(IPaddress.objects.bulk_create(objectlist))