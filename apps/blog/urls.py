from django.conf.urls.defaults import *
from kusskr.apps.blog import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name="blog-index", kwargs={"page_no": 1}),
    (r'^(\d*)/$', views.index),
    # Example:
    # (r'^kusskr/', include('kusskr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
