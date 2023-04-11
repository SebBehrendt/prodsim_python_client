# swagger_client.ScenarioApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scenario_projects_project_id_adapters_adapter_id_scenario_put**](ScenarioApi.md#create_scenario_projects_project_id_adapters_adapter_id_scenario_put) | **PUT** /projects/{project_id}/adapters/{adapter_id}/scenario | Create Scenario
[**read_scenario_projects_project_id_adapters_adapter_id_scenario_get**](ScenarioApi.md#read_scenario_projects_project_id_adapters_adapter_id_scenario_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/scenario | Read Scenario

# **create_scenario_projects_project_id_adapters_adapter_id_scenario_put**
> object create_scenario_projects_project_id_adapters_adapter_id_scenario_put(body, project_id, adapter_id)

Create Scenario

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScenarioApi()
body = swagger_client.ScenarioData() # ScenarioData | 
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Create Scenario
    api_response = api_instance.create_scenario_projects_project_id_adapters_adapter_id_scenario_put(body, project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScenarioApi->create_scenario_projects_project_id_adapters_adapter_id_scenario_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScenarioData**](ScenarioData.md)|  | 
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_scenario_projects_project_id_adapters_adapter_id_scenario_get**
> ScenarioData read_scenario_projects_project_id_adapters_adapter_id_scenario_get(project_id, adapter_id)

Read Scenario

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScenarioApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Read Scenario
    api_response = api_instance.read_scenario_projects_project_id_adapters_adapter_id_scenario_get(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScenarioApi->read_scenario_projects_project_id_adapters_adapter_id_scenario_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

[**ScenarioData**](ScenarioData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

