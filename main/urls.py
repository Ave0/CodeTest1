from django.conf.urls import url
from django.contrib import admin
from django.urls.conf import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from main import views

urlpatterns = [

  url('api-auth/', include('rest_framework.urls')),
  url('contactlistall/', views.ListContactView.as_view(), name="List all Contacts"),
  url('update/(?P<pk>[0-9]+)/$', views.SingleContactView.as_view(), name="Update or Delete Contact"),

]
