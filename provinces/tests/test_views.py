from collections import OrderedDict

from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from provinces.models import Province, Country
from provinces.views import UserList

class ProvinceViewTest(TestCase):

    def setUp(self):
        user = User.objects.create_user('Ryan', 'ryan-diplomacy@mailinator.com', 'password')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'password')
        country = Country.objects.create(country_name=Country.ENGLAND, player=user)
        Province.objects.create(
            name='London', abbr='LON', owner=country,
            province_type=Province.COASTAL, supply_center=True
        )

    def test_non_admin_user_can_not_see_users(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='Ryan')
        view = UserList.as_view()
        request = factory.get('/users.json')
        force_authenticate(request, user=user)
        response = view(request)
        expected_response = {'detail': 'You do not have permission to perform this action.'}
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, expected_response)

    def test_returns_user_list(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='admin')
        view = UserList.as_view()
        request = factory.get('/users.json')
        force_authenticate(request, user=user)
        response = view(request)
        user_response = OrderedDict([('count', 2), ('next', None), ('previous', None), ('results', [OrderedDict([('id', 1), ('username', 'Ryan'), ('country', [1])]), OrderedDict([('id', 2), ('username', 'admin'), ('country', [])])])])
        self.assertEqual(user_response, response.data)
