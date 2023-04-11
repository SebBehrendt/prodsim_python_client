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
from swagger_client.api.states_api import StatesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStatesApi(unittest.TestCase):
    """StatesApi unit test stubs"""

    def setUp(self):
        self.api = StatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_state_projects_project_id_adapters_adapter_id_states_state_id_put(self):
        """Test case for create_state_projects_project_id_adapters_adapter_id_states_state_id_put

        Create State  # noqa: E501
        """
        pass

    def test_read_state_projects_project_id_adapters_adapter_id_states_state_id_get(self):
        """Test case for read_state_projects_project_id_adapters_adapter_id_states_state_id_get

        Read State  # noqa: E501
        """
        pass

    def test_read_states_projects_project_id_adapters_adapter_id_states_get(self):
        """Test case for read_states_projects_project_id_adapters_adapter_id_states_get

        Read States  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()