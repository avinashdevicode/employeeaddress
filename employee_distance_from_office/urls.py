from django.conf.urls import patterns, include, url
from distance import urls as URL

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       
                       url(r'dis/', include(URL))
    # Examples:
    # url(r'^$', 'employee_distance_from_office.views.home', name='home'),
    # url(r'^employee_distance_from_office/', include('employee_distance_from_office.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
