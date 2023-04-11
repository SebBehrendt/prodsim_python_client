# swagger_client.SimulationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_simulation_projects_project_id_adapters_adapter_id_run_simulation_get**](SimulationApi.md#run_simulation_projects_project_id_adapters_adapter_id_run_simulation_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/run_simulation | Run Simulation

# **run_simulation_projects_project_id_adapters_adapter_id_run_simulation_get**
> str run_simulation_projects_project_id_adapters_adapter_id_run_simulation_get(project_id, adapter_id)

Run Simulation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SimulationApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Run Simulation
    api_response = api_instance.run_simulation_projects_project_id_adapters_adapter_id_run_simulation_get(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationApi->run_simulation_projects_project_id_adapters_adapter_id_run_simulation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

