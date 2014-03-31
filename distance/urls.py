'''
Created on Mar 31, 2014

@author: avinash
'''
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       
                       url(r'', 'distance.views.empAddressView'),
    # Examples:
    # url(r'^$', 'employee_distance_from_office.views.home', name='home'),
    # url(r'^employee_distance_from_office/', include('employee_distance_from_office.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
