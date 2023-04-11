# swagger_client.ResourcesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_projects_project_id_adapters_adapter_id_resources_resource_id_put**](ResourcesApi.md#create_resource_projects_project_id_adapters_adapter_id_resources_resource_id_put) | **PUT** /projects/{project_id}/adapters/{adapter_id}/resources/{resource_id} | Create Resource
[**delete_resource_projects_project_id_adapters_adapter_id_resources_resource_id_delete**](ResourcesApi.md#delete_resource_projects_project_id_adapters_adapter_id_resources_resource_id_delete) | **DELETE** /projects/{project_id}/adapters/{adapter_id}/resources/{resource_id} | Delete Resource
[**read_resource_projects_project_id_adapters_adapter_id_resources_resource_id_get**](ResourcesApi.md#read_resource_projects_project_id_adapters_adapter_id_resources_resource_id_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/resources/{resource_id} | Read Resource
[**read_resources_projects_project_id_adapters_adapter_id_resources_get**](ResourcesApi.md#read_resources_projects_project_id_adapters_adapter_id_resources_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/resources | Read Resources

# **create_resource_projects_project_id_adapters_adapter_id_resources_resource_id_put**
> object create_resource_projects_project_id_adapters_adapter_id_resources_resource_id_put(body, project_id, adapter_id, resource_id)

Create Resource

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesApi()
body = swagger_client.Resource() # Resource | 
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
resource_id = 'resource_id_example' # str | 

try:
    # Create Resource
    api_response = api_instance.create_resource_projects_project_id_adapters_adapter_id_resources_resource_id_put(body, project_id, adapter_id, resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->create_resource_projects_project_id_adapters_adapter_id_resources_resource_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Resource**](Resource.md)|  | 
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **resource_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_projects_project_id_adapters_adapter_id_resources_resource_id_delete**
> object delete_resource_projects_project_id_adapters_adapter_id_resources_resource_id_delete(project_id, adapter_id, resource_id)

Delete Resource

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
resource_id = 'resource_id_example' # str | 

try:
    # Delete Resource
    api_response = api_instance.delete_resource_projects_project_id_adapters_adapter_id_resources_resource_id_delete(project_id, adapter_id, resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->delete_resource_projects_project_id_adapters_adapter_id_resources_resource_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **resource_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_resource_projects_project_id_adapters_adapter_id_resources_resource_id_get**
> ResponseReadResourceProjectsProjectIdAdaptersAdapterIdResourcesResourceIdGet read_resource_projects_project_id_adapters_adapter_id_resources_resource_id_get(project_id, adapter_id, resource_id)

Read Resource

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
resource_id = 'resource_id_example' # str | 

try:
    # Read Resource
    api_response = api_instance.read_resource_projects_project_id_adapters_adapter_id_resources_resource_id_get(project_id, adapter_id, resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->read_resource_projects_project_id_adapters_adapter_id_resources_resource_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **resource_id** | **str**|  | 

### Return type

[**ResponseReadResourceProjectsProjectIdAdaptersAdapterIdResourcesResourceIdGet**](ResponseReadResourceProjectsProjectIdAdaptersAdapterIdResourcesResourceIdGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_resources_projects_project_id_adapters_adapter_id_resources_get**
> list[object] read_resources_projects_project_id_adapters_adapter_id_resources_get(project_id, adapter_id)

Read Resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Read Resources
    api_response = api_instance.read_resources_projects_project_id_adapters_adapter_id_resources_get(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->read_resources_projects_project_id_adapters_adapter_id_resources_get: %s\n" % e)
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

