# swagger_client.SinksApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_put**](SinksApi.md#create_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_put) | **PUT** /projects/{project_id}/adapters/{adapter_id}/sinks/{sink_id} | Create Sink
[**read_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_get**](SinksApi.md#read_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/sinks/{sink_id} | Read Sink
[**read_sinks_projects_project_id_adapters_adapter_id_sinks_get**](SinksApi.md#read_sinks_projects_project_id_adapters_adapter_id_sinks_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/sinks | Read Sinks

# **create_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_put**
> object create_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_put(body, project_id, adapter_id, sink_id)

Create Sink

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SinksApi()
body = swagger_client.SinkData() # SinkData | 
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
sink_id = NULL # object | 

try:
    # Create Sink
    api_response = api_instance.create_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_put(body, project_id, adapter_id, sink_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SinksApi->create_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SinkData**](SinkData.md)|  | 
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **sink_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_get**
> SinkData read_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_get(project_id, adapter_id, sink_id)

Read Sink

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SinksApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
sink_id = 'sink_id_example' # str | 

try:
    # Read Sink
    api_response = api_instance.read_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_get(project_id, adapter_id, sink_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SinksApi->read_sink_projects_project_id_adapters_adapter_id_sinks_sink_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **sink_id** | **str**|  | 

### Return type

[**SinkData**](SinkData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_sinks_projects_project_id_adapters_adapter_id_sinks_get**
> list[SinkData] read_sinks_projects_project_id_adapters_adapter_id_sinks_get(project_id, adapter_id)

Read Sinks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SinksApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Read Sinks
    api_response = api_instance.read_sinks_projects_project_id_adapters_adapter_id_sinks_get(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SinksApi->read_sinks_projects_project_id_adapters_adapter_id_sinks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

[**list[SinkData]**](SinkData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

