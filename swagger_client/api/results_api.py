# coding: utf-8

"""
    ProdSim API

     The ProdSim-API allows you to create and run production simulations and optimizations with the ProdSim library.    # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: sebastianbehrendt97@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ResultsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_results_projects_project_id_adapters_adapter_id_results_static_results_get(self, project_id, adapter_id, **kwargs):  # noqa: E501
        """Get All Results  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_results_projects_project_id_adapters_adapter_id_results_static_results_get(project_id, adapter_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str adapter_id: (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_results_projects_project_id_adapters_adapter_id_results_static_results_get_with_http_info(project_id, adapter_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_results_projects_project_id_adapters_adapter_id_results_static_results_get_with_http_info(project_id, adapter_id, **kwargs)  # noqa: E501
            return data

    def get_all_results_projects_project_id_adapters_adapter_id_results_static_results_get_with_http_info(self, project_id, adapter_id, **kwargs):  # noqa: E501
        """Get All Results  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_results_projects_project_id_adapters_adapter_id_results_static_results_get_with_http_info(project_id, adapter_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str adapter_id: (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'adapter_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_results_projects_project_id_adapters_adapter_id_results_static_results_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `get_all_results_projects_project_id_adapters_adapter_id_results_static_results_get`")  # noqa: E501
        # verify the required parameter 'adapter_id' is set
        if ('adapter_id' not in params or
                params['adapter_id'] is None):
            raise ValueError("Missing the required parameter `adapter_id` when calling `get_all_results_projects_project_id_adapters_adapter_id_results_static_results_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['project_id'] = params['project_id']  # noqa: E501
        if 'adapter_id' in params:
            path_params['adapter_id'] = params['adapter_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_id}/adapters/{adapter_id}/results/static_results', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_event_results_projects_project_id_adapters_adapter_id_results_event_results_get(self, project_id, adapter_id, **kwargs):  # noqa: E501
        """Get Event Results  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event_results_projects_project_id_adapters_adapter_id_results_event_results_get(project_id, adapter_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str adapter_id: (required)
        :return: list[Event]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_event_results_projects_project_id_adapters_adapter_id_results_event_results_get_with_http_info(project_id, adapter_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_event_results_projects_project_id_adapters_adapter_id_results_event_results_get_with_http_info(project_id, adapter_id, **kwargs)  # noqa: E501
            return data

    def get_event_results_projects_project_id_adapters_adapter_id_results_event_results_get_with_http_info(self, project_id, adapter_id, **kwargs):  # noqa: E501
        """Get Event Results  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event_results_projects_project_id_adapters_adapter_id_results_event_results_get_with_http_info(project_id, adapter_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str adapter_id: (required)
        :return: list[Event]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'adapter_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_event_results_projects_project_id_adapters_adapter_id_results_event_results_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `get_event_results_projects_project_id_adapters_adapter_id_results_event_results_get`")  # noqa: E501
        # verify the required parameter 'adapter_id' is set
        if ('adapter_id' not in params or
                params['adapter_id'] is None):
            raise ValueError("Missing the required parameter `adapter_id` when calling `get_event_results_projects_project_id_adapters_adapter_id_results_event_results_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['project_id'] = params['project_id']  # noqa: E501
        if 'adapter_id' in params:
            path_params['adapter_id'] = params['adapter_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_id}/adapters/{adapter_id}/results/event_results', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Event]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get(self, project_id, adapter_id, kpi, **kwargs):  # noqa: E501
        """Get Output Results  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get(project_id, adapter_id, kpi, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str adapter_id: (required)
        :param KPIEnum kpi: (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get_with_http_info(project_id, adapter_id, kpi, **kwargs)  # noqa: E501
        else:
            (data) = self.get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get_with_http_info(project_id, adapter_id, kpi, **kwargs)  # noqa: E501
            return data

    def get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get_with_http_info(self, project_id, adapter_id, kpi, **kwargs):  # noqa: E501
        """Get Output Results  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get_with_http_info(project_id, adapter_id, kpi, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str adapter_id: (required)
        :param KPIEnum kpi: (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'adapter_id', 'kpi']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get`")  # noqa: E501
        # verify the required parameter 'adapter_id' is set
        if ('adapter_id' not in params or
                params['adapter_id'] is None):
            raise ValueError("Missing the required parameter `adapter_id` when calling `get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get`")  # noqa: E501
        # verify the required parameter 'kpi' is set
        if ('kpi' not in params or
                params['kpi'] is None):
            raise ValueError("Missing the required parameter `kpi` when calling `get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['project_id'] = params['project_id']  # noqa: E501
        if 'adapter_id' in params:
            path_params['adapter_id'] = params['adapter_id']  # noqa: E501
        if 'kpi' in params:
            path_params['kpi'] = params['kpi']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_id}/adapters/{adapter_id}/results/{kpi}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
