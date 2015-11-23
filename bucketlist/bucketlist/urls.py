from django.conf.urls import include, url
from django.contrib import admin

from main.views import IndexView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', include('main.urls', namespace='dashboard')),
    url(r'^$', IndexView.as_view(), name='home'),
]
