# swagger_client.StatesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_state_projects_project_id_adapters_adapter_id_states_state_id_put**](StatesApi.md#create_state_projects_project_id_adapters_adapter_id_states_state_id_put) | **PUT** /projects/{project_id}/adapters/{adapter_id}/states/{state_id} | Create State
[**read_state_projects_project_id_adapters_adapter_id_states_state_id_get**](StatesApi.md#read_state_projects_project_id_adapters_adapter_id_states_state_id_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/states/{state_id} | Read State
[**read_states_projects_project_id_adapters_adapter_id_states_get**](StatesApi.md#read_states_projects_project_id_adapters_adapter_id_states_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/states | Read States

# **create_state_projects_project_id_adapters_adapter_id_states_state_id_put**
> object create_state_projects_project_id_adapters_adapter_id_states_state_id_put(body, project_id, adapter_id, state_id)

Create State

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatesApi()
body = swagger_client.StateData() # StateData | 
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
state_id = NULL # object | 

try:
    # Create State
    api_response = api_instance.create_state_projects_project_id_adapters_adapter_id_states_state_id_put(body, project_id, adapter_id, state_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatesApi->create_state_projects_project_id_adapters_adapter_id_states_state_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StateData**](StateData.md)|  | 
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **state_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_state_projects_project_id_adapters_adapter_id_states_state_id_get**
> StateData read_state_projects_project_id_adapters_adapter_id_states_state_id_get(project_id, adapter_id, state_id)

Read State

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatesApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
state_id = 'state_id_example' # str | 

try:
    # Read State
    api_response = api_instance.read_state_projects_project_id_adapters_adapter_id_states_state_id_get(project_id, adapter_id, state_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatesApi->read_state_projects_project_id_adapters_adapter_id_states_state_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **state_id** | **str**|  | 

### Return type

[**StateData**](StateData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_states_projects_project_id_adapters_adapter_id_states_get**
> list[StateData] read_states_projects_project_id_adapters_adapter_id_states_get(project_id, adapter_id)

Read States

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatesApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Read States
    api_response = api_instance.read_states_projects_project_id_adapters_adapter_id_states_get(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatesApi->read_states_projects_project_id_adapters_adapter_id_states_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

[**list[StateData]**](StateData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

