from django.contrib.auth.models import User

from rest_framework import generics, permissions

from provinces.models import Country, Province
from provinces.serializers import CountrySerializer, ProvinceSerializer, UserSerializer

class ProvinceList(generics.ListAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class ProvinceDetail(generics.RetrieveAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = ProvinceSerializer

class CountryDetail(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = ProvinceSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
