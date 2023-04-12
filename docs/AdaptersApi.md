# swagger_client.AdaptersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_adapter_projects_project_id_adapters_adapter_id_delete**](AdaptersApi.md#delete_adapter_projects_project_id_adapters_adapter_id_delete) | **DELETE** /projects/{project_id}/adapters/{adapter_id} | Delete Adapter
[**read_adapter_projects_project_id_adapters_adapter_id_get**](AdaptersApi.md#read_adapter_projects_project_id_adapters_adapter_id_get) | **GET** /projects/{project_id}/adapters/{adapter_id} | Read Adapter
[**read_adapters_projects_project_id_adapters_get**](AdaptersApi.md#read_adapters_projects_project_id_adapters_get) | **GET** /projects/{project_id}/adapters | Read Adapters
[**update_adapter_projects_project_id_adapters_adapter_id_put**](AdaptersApi.md#update_adapter_projects_project_id_adapters_adapter_id_put) | **PUT** /projects/{project_id}/adapters/{adapter_id} | Update Adapter

# **delete_adapter_projects_project_id_adapters_adapter_id_delete**
> object delete_adapter_projects_project_id_adapters_adapter_id_delete(project_id, adapter_id)

Delete Adapter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdaptersApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Delete Adapter
    api_response = api_instance.delete_adapter_projects_project_id_adapters_adapter_id_delete(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdaptersApi->delete_adapter_projects_project_id_adapters_adapter_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_adapter_projects_project_id_adapters_adapter_id_get**
> JsonAdapter read_adapter_projects_project_id_adapters_adapter_id_get(project_id, adapter_id)

Read Adapter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdaptersApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Read Adapter
    api_response = api_instance.read_adapter_projects_project_id_adapters_adapter_id_get(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdaptersApi->read_adapter_projects_project_id_adapters_adapter_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

[**JsonAdapter**](JsonAdapter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_adapters_projects_project_id_adapters_get**
> dict(str, JsonAdapter) read_adapters_projects_project_id_adapters_get(project_id)

Read Adapters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdaptersApi()
project_id = 'project_id_example' # str | 

try:
    # Read Adapters
    api_response = api_instance.read_adapters_projects_project_id_adapters_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdaptersApi->read_adapters_projects_project_id_adapters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**dict(str, JsonAdapter)**](JsonAdapter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_adapter_projects_project_id_adapters_adapter_id_put**
> object update_adapter_projects_project_id_adapters_adapter_id_put(body, project_id, adapter_id)

Update Adapter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdaptersApi()
body = swagger_client.JsonAdapter() # JsonAdapter | 
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Update Adapter
    api_response = api_instance.update_adapter_projects_project_id_adapters_adapter_id_put(body, project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdaptersApi->update_adapter_projects_project_id_adapters_adapter_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAdapter**](JsonAdapter.md)|  | 
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

