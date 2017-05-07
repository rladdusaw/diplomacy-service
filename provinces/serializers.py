from django.contrib.auth.models import User

from rest_framework import serializers

from provinces.models import Country, Province

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country_name',)
        player = serializers.ReadOnlyField(source='player.username')

class UserSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(many=True, queryset=Country.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'country')

class ProvinceSerializer(serializers.ModelSerializer):
    provinces = serializers.PrimaryKeyRelatedField(many=True, queryset=Province.objects.all())

    class Meta:
        model = Province
        fields = ('name', 'abbr', 'owner', 'province_type')
