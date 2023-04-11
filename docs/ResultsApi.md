# swagger_client.ResultsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_results_projects_project_id_adapters_adapter_id_results_static_results_get**](ResultsApi.md#get_all_results_projects_project_id_adapters_adapter_id_results_static_results_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/results/static_results | Get All Results
[**get_event_results_projects_project_id_adapters_adapter_id_results_event_results_get**](ResultsApi.md#get_event_results_projects_project_id_adapters_adapter_id_results_event_results_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/results/event_results | Get Event Results
[**get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get**](ResultsApi.md#get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/results/{kpi} | Get Output Results

# **get_all_results_projects_project_id_adapters_adapter_id_results_static_results_get**
> list[object] get_all_results_projects_project_id_adapters_adapter_id_results_static_results_get(project_id, adapter_id)

Get All Results

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultsApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Get All Results
    api_response = api_instance.get_all_results_projects_project_id_adapters_adapter_id_results_static_results_get(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultsApi->get_all_results_projects_project_id_adapters_adapter_id_results_static_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_results_projects_project_id_adapters_adapter_id_results_event_results_get**
> list[Event] get_event_results_projects_project_id_adapters_adapter_id_results_event_results_get(project_id, adapter_id)

Get Event Results

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultsApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Get Event Results
    api_response = api_instance.get_event_results_projects_project_id_adapters_adapter_id_results_event_results_get(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultsApi->get_event_results_projects_project_id_adapters_adapter_id_results_event_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get**
> list[object] get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get(project_id, adapter_id, kpi)

Get Output Results

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultsApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
kpi = swagger_client.KPIEnum() # KPIEnum | 

try:
    # Get Output Results
    api_response = api_instance.get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get(project_id, adapter_id, kpi)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultsApi->get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **kpi** | [**KPIEnum**](.md)|  | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

