# swagger_client.SourcesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_source_projects_project_id_adapters_adapter_id_sources_source_id_put**](SourcesApi.md#create_source_projects_project_id_adapters_adapter_id_sources_source_id_put) | **PUT** /projects/{project_id}/adapters/{adapter_id}/sources/{source_id} | Create Source
[**read_source_projects_project_id_adapters_adapter_id_sources_source_id_get**](SourcesApi.md#read_source_projects_project_id_adapters_adapter_id_sources_source_id_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/sources/{source_id} | Read Source
[**read_sources_projects_project_id_adapters_adapter_id_sources_get**](SourcesApi.md#read_sources_projects_project_id_adapters_adapter_id_sources_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/sources | Read Sources

# **create_source_projects_project_id_adapters_adapter_id_sources_source_id_put**
> object create_source_projects_project_id_adapters_adapter_id_sources_source_id_put(body, project_id, adapter_id, source_id)

Create Source

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SourcesApi()
body = swagger_client.SourceData() # SourceData | 
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
source_id = NULL # object | 

try:
    # Create Source
    api_response = api_instance.create_source_projects_project_id_adapters_adapter_id_sources_source_id_put(body, project_id, adapter_id, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->create_source_projects_project_id_adapters_adapter_id_sources_source_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceData**](SourceData.md)|  | 
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **source_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_source_projects_project_id_adapters_adapter_id_sources_source_id_get**
> SourceData read_source_projects_project_id_adapters_adapter_id_sources_source_id_get(project_id, adapter_id, source_id)

Read Source

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SourcesApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
source_id = 'source_id_example' # str | 

try:
    # Read Source
    api_response = api_instance.read_source_projects_project_id_adapters_adapter_id_sources_source_id_get(project_id, adapter_id, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->read_source_projects_project_id_adapters_adapter_id_sources_source_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **source_id** | **str**|  | 

### Return type

[**SourceData**](SourceData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_sources_projects_project_id_adapters_adapter_id_sources_get**
> list[SourceData] read_sources_projects_project_id_adapters_adapter_id_sources_get(project_id, adapter_id)

Read Sources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SourcesApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Read Sources
    api_response = api_instance.read_sources_projects_project_id_adapters_adapter_id_sources_get(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->read_sources_projects_project_id_adapters_adapter_id_sources_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

[**list[SourceData]**](SourceData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

