from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from provinces import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^provinces/$', views.ProvinceList.as_view()),
    url(r'^provinces/(?P<pk>[0-9]+)/$', views.ProvinceDetail.as_view()),
    url(r'^countries/$', views.CountryList.as_view()),
    url(r'^countries/(?P<pk>[0-9]+)/$', views.CountryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
