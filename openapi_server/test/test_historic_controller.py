# coding: utf-8

from __future__ import absolute_import

from unittest import mock

from flask import json
from six import BytesIO

from openapi_server.models.visit import Visit  # noqa: E501
from openapi_server.test import BaseTestCase


class TestHistoricController(BaseTestCase):
    """HistoricController integration test stubs"""

    @mock.patch("muii_g2_family_lock_database.Database.PostgresDB.add_visit")
    def test_add_visit(self, mocked_add_visit):
        """Test case for add_visit

        Add a visit to historic
        """
        visit = Visit()
        mocked_add_visit.assert_not_called()
        mocked_add_visit.return_value = None
        response = self.client.open(
            '/historic',
            method='POST',
            data=json.dumps(visit),
            content_type='application/json')
        mocked_add_visit.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @mock.patch("muii_g2_family_lock_database.Database.PostgresDB.get_all_historic")
    def test_get_all_historic(self, mocked_get_all_historic):
        """Test case for get_all_historic

        Get all visits from historic
        """
        mocked_get_all_historic.assert_not_called()
        mocked_get_all_historic.return_value = [
            [
                "27/11/2020",
                1,
                "ff:ff:ff:ff:ff:ff",
                "2:07"
            ],
            [
                "27/11/2020",
                2,
                "00:00:00:00:00",
                "2:07"
            ],
            [
                "27/11/2020",
                3,
                "00:00:00:00:00",
                "2:07"
            ]
        ]
        response = self.client.open(
            '/historic',
            method='GET')
        mocked_get_all_historic.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @mock.patch("muii_g2_family_lock_database.Database.PostgresDB.get_visit")
    def test_get_visit(self, mocked_get_visit):
        """Test case for get_visit

        Get one visit's information
        """
        mocked_get_visit.assert_not_called()
        mocked_get_visit.return_value = [
            [
                "27/11/2020",
                1,
                "ff:ff:ff:ff:ff:ff",
                "2:07"
            ],
        ]
        response = self.client.open(
            '/historic/{id}'.format(id=3),
            method='GET')
        mocked_get_visit.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
