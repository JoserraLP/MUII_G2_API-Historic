# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.visit import Visit  # noqa: E501
from openapi_server.test import BaseTestCase


class TestHistoricController(BaseTestCase):
    """HistoricController integration test stubs"""

    def test_add_visit(self):
        """Test case for add_visit

        Add a visit to historic
        """
        visit = Visit()
        response = self.client.open(
            '/historic',
            method='POST',
            data=json.dumps(visit),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_historic(self):
        """Test case for get_all_historic

        Get all visits from historic
        """
        response = self.client.open(
            '/historic',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_visit(self):
        """Test case for get_visit

        Get one visit's information
        """
        response = self.client.open(
            '/historic/{id}'.format(id=3),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
