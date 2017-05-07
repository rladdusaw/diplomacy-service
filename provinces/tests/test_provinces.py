import json

from django.test import TestCase

from diplomacyservice.config import DEFAULT_BOARD_SETUP
from provinces.models import Province

class DefaultSetupTest(TestCase):

    def test_75_provinces(self):
        data = json.loads(DEFAULT_BOARD_SETUP)
        count = 0
        for item in data:
            count += 1
        self.assertEqual(count, 75)

    def test_neighbors_match(self):
        data = json.loads(DEFAULT_BOARD_SETUP)
        missmatch = False
        errors = {}
        for province in data:
            for neighbor in province['neighbors']:
                neighbors = self.get_neighbor_by_abbr(neighbor)['neighbors']
                if province['abbr'] not in neighbors:
                    missmatch = True
                    errors[province['name']] = neighbor
        self.assertFalse(missmatch, errors)

    def get_neighbor_by_abbr(self, abbr):
        data = json.loads(DEFAULT_BOARD_SETUP)
        for province in data:
            if province['abbr'] == abbr:
                return province
