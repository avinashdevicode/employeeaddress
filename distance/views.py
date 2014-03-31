# Create your views here.

from django.shortcuts import render_to_response
from distance.models import Address
from django.core.context_processors import csrf
from django.template.context import RequestContext

def empAddressView(request):
    if request.method == 'POST':
        lat = float(request.POST['latFld'])
        lng = float(request.POST['lngFld'])
        print 1
        print str(request.POST['outputdiv'])
        print 2
        addres = str(request.POST['outputdiv']).split("...")[0]
        dist = str(request.POST['outputdiv']).split("...")[1].split()[0]
        address = Address(lat=lat, lng=lng, addres = addres, dist = dist)
        address.save()
        return render_to_response('success.html')
    
    c = {}
    c.update(csrf(request))
    return render_to_response('googlemap.html', context_instance = RequestContext(request, c))