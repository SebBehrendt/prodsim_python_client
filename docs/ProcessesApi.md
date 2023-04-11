# swagger_client.ProcessesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_process_projects_project_id_adapters_adapter_id_processes_process_id_put**](ProcessesApi.md#create_process_projects_project_id_adapters_adapter_id_processes_process_id_put) | **PUT** /projects/{project_id}/adapters/{adapter_id}/processes/{process_id} | Create Process
[**read_process_projects_project_id_adapters_adapter_id_processes_process_id_get**](ProcessesApi.md#read_process_projects_project_id_adapters_adapter_id_processes_process_id_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/processes/{process_id} | Read Process
[**read_processes_projects_project_id_adapters_adapter_id_processes_get**](ProcessesApi.md#read_processes_projects_project_id_adapters_adapter_id_processes_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/processes | Read Processes

# **create_process_projects_project_id_adapters_adapter_id_processes_process_id_put**
> object create_process_projects_project_id_adapters_adapter_id_processes_process_id_put(body, project_id, adapter_id, process_id)

Create Process

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProcessesApi()
body = swagger_client.ProcessData() # ProcessData | 
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
process_id = NULL # object | 

try:
    # Create Process
    api_response = api_instance.create_process_projects_project_id_adapters_adapter_id_processes_process_id_put(body, project_id, adapter_id, process_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessesApi->create_process_projects_project_id_adapters_adapter_id_processes_process_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProcessData**](ProcessData.md)|  | 
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **process_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_process_projects_project_id_adapters_adapter_id_processes_process_id_get**
> ProcessData read_process_projects_project_id_adapters_adapter_id_processes_process_id_get(project_id, adapter_id, process_id)

Read Process

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProcessesApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
process_id = 'process_id_example' # str | 

try:
    # Read Process
    api_response = api_instance.read_process_projects_project_id_adapters_adapter_id_processes_process_id_get(project_id, adapter_id, process_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessesApi->read_process_projects_project_id_adapters_adapter_id_processes_process_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **process_id** | **str**|  | 

### Return type

[**ProcessData**](ProcessData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_processes_projects_project_id_adapters_adapter_id_processes_get**
> list[ProcessData] read_processes_projects_project_id_adapters_adapter_id_processes_get(project_id, adapter_id)

Read Processes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProcessesApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Read Processes
    api_response = api_instance.read_processes_projects_project_id_adapters_adapter_id_processes_get(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessesApi->read_processes_projects_project_id_adapters_adapter_id_processes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

[**list[ProcessData]**](ProcessData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

