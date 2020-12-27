from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Vlan, IPaddress
from .forms import VlanForm, IPAddressForm
from django.shortcuts import reverse
from django.forms import inlineformset_factory

class VlanListView(ListView):
    model = Vlan
    template_name = 'Vlans/vlan_list.html'
    context_object_name = 'vlans'

class VlanDetailView(DetailView):
    model = Vlan
    
class IPAddressUpdateView(UpdateView):
    template_name = 'Vlans/ipaddress_update.html'
    form_class = IPAddressForm
    model = IPaddress
    #context_object_name = "ipaddress"

    def get_success_url(self):
        return reverse('vlans:vlan_detail',kwargs={ 'pk':self.object.vlan.id })

def edit_multiple_ipaddresses(request, vlan_number):
    vlan = Vlan.objects.get(number=vlan_number)
    IPaddressFormSet = inlineformset_factory(
            parent_model = Vlan, 
            model = IPaddress, 
            form=IPAddressForm, 
            fields=('ipaddress','description','used',),
            can_delete=False,
            extra=0,
            )
    if request.method == "GET":
        formset = IPaddressFormSet(instance=vlan)
        ctx = { 'formset':formset, 'vlan_number': vlan.number}
        return render(request, template_name="Vlans/ipaddress_medit.html", context=ctx)
    if request.method == "POST":
        formset = IPaddressFormSet(request.POST, instance=vlan)
        if formset.is_valid():
            formset.save()
            #return HttpResponse("formset is valid saved")
            #return reverse('vlans:vlan_detail', kwargs={ 'pk':pk })
            return HttpResponseRedirect(reverse('vlans:vlan_detail', kwargs={ 'pk':vlan.pk }))
            #reverse() returns a string. form_valid() is supposed to return HTTP responses, not strings.
        else:
            #vlan = Vlan.objects.get(id=pk)
            #formset = IPaddressFormSet(instance=vlan)
            ctx = { 'formset':formset}
            return HttpResponse("formset is not valid")
            #return render(request, template_name="Vlans/ipaddress_medit.html", context=ctx)