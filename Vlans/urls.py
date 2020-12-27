from django.urls import path, include
from .views import (
    VlanListView,
    VlanDetailView,
    IPAddressUpdateView,
    edit_multiple_ipaddresses
)

app_name = "vlans"

urlpatterns = [
    path('', VlanListView.as_view(), name="vlan_list"),
    path('vlan/<int:pk>/', VlanDetailView.as_view(), name="vlan_detail"),
    path('ipaddress/edit/<int:pk>/', IPAddressUpdateView.as_view(), name="ipaddress_update"),
    path('ipaddress/multipleedit/vlan/<int:vlan_number>', edit_multiple_ipaddresses, name='multi_ipedit')
]