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
from swagger_client.api.time_models_api import TimeModelsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTimeModelsApi(unittest.TestCase):
    """TimeModelsApi unit test stubs"""

    def setUp(self):
        self.api = TimeModelsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_put(self):
        """Test case for create_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_put

        Create Time Model  # noqa: E501
        """
        pass

    def test_read_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_get(self):
        """Test case for read_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_get

        Read Time Model  # noqa: E501
        """
        pass

    def test_read_time_models_projects_project_id_adapters_adapter_id_time_models_get(self):
        """Test case for read_time_models_projects_project_id_adapters_adapter_id_time_models_get

        Read Time Models  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
