# swagger_client.QueuesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_queue_projects_project_id_adapters_adapter_id_queues_queue_id_put**](QueuesApi.md#create_queue_projects_project_id_adapters_adapter_id_queues_queue_id_put) | **PUT** /projects/{project_id}/adapters/{adapter_id}/queues/{queue_id} | Create Queue
[**read_queue_projects_project_id_adapters_adapter_id_queues_queue_id_get**](QueuesApi.md#read_queue_projects_project_id_adapters_adapter_id_queues_queue_id_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/queues/{queue_id} | Read Queue
[**read_queues_projects_project_id_adapters_adapter_id_queues_get**](QueuesApi.md#read_queues_projects_project_id_adapters_adapter_id_queues_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/queues | Read Queues

# **create_queue_projects_project_id_adapters_adapter_id_queues_queue_id_put**
> object create_queue_projects_project_id_adapters_adapter_id_queues_queue_id_put(body, project_id, adapter_id, queue_id)

Create Queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueuesApi()
body = swagger_client.QueueData() # QueueData | 
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
queue_id = NULL # object | 

try:
    # Create Queue
    api_response = api_instance.create_queue_projects_project_id_adapters_adapter_id_queues_queue_id_put(body, project_id, adapter_id, queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueuesApi->create_queue_projects_project_id_adapters_adapter_id_queues_queue_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QueueData**](QueueData.md)|  | 
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **queue_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_queue_projects_project_id_adapters_adapter_id_queues_queue_id_get**
> QueueData read_queue_projects_project_id_adapters_adapter_id_queues_queue_id_get(project_id, adapter_id, queue_id)

Read Queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueuesApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
queue_id = 'queue_id_example' # str | 

try:
    # Read Queue
    api_response = api_instance.read_queue_projects_project_id_adapters_adapter_id_queues_queue_id_get(project_id, adapter_id, queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueuesApi->read_queue_projects_project_id_adapters_adapter_id_queues_queue_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **queue_id** | **str**|  | 

### Return type

[**QueueData**](QueueData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_queues_projects_project_id_adapters_adapter_id_queues_get**
> list[QueueData] read_queues_projects_project_id_adapters_adapter_id_queues_get(project_id, adapter_id)

Read Queues

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueuesApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Read Queues
    api_response = api_instance.read_queues_projects_project_id_adapters_adapter_id_queues_get(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueuesApi->read_queues_projects_project_id_adapters_adapter_id_queues_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

[**list[QueueData]**](QueueData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

