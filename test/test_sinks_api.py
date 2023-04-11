# coding: utf-8

"""
    ProdSim API

     The ProdSim-API allows you to create and run production simulations and optimizations with the ProdSim library.    # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: sebastianbehrendt97@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.sinks_api import SinksApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSinksApi(unittest.TestCase):
    """SinksApi unit test stubs"""

    def setUp(self):
        self.api = SinksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_put(self):
        """Test case for create_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_put

        Create Sink  # noqa: E501
        """
        pass

    def test_read_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_get(self):
        """Test case for read_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_get

        Read Sink  # noqa: E501
        """
        pass

    def test_read_sinks_projects_project_id_adapters_adapter_id_sinks_get(self):
        """Test case for read_sinks_projects_project_id_adapters_adapter_id_sinks_get

        Read Sinks  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
