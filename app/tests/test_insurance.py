import pytest


class TestInsurance:
    def setUp(self):
        self.insurance = Insurance()

    def test_one(self):
        assert self.insurance.get_auto() == None