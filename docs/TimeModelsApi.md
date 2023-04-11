# swagger_client.TimeModelsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_put**](TimeModelsApi.md#create_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_put) | **PUT** /projects/{project_id}/adapters/{adapter_id}/time_models/{time_model_id} | Create Time Model
[**read_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_get**](TimeModelsApi.md#read_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/time_models/{time_model_id} | Read Time Model
[**read_time_models_projects_project_id_adapters_adapter_id_time_models_get**](TimeModelsApi.md#read_time_models_projects_project_id_adapters_adapter_id_time_models_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/time_models | Read Time Models

# **create_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_put**
> object create_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_put(body, project_id, adapter_id, time_model_id)

Create Time Model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TimeModelsApi()
body = swagger_client.TimeModel() # TimeModel | 
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
time_model_id = NULL # object | 

try:
    # Create Time Model
    api_response = api_instance.create_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_put(body, project_id, adapter_id, time_model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeModelsApi->create_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimeModel**](TimeModel.md)|  | 
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **time_model_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_get**
> ResponseReadTimeModelProjectsProjectIdAdaptersAdapterIdTimeModelsTimeModelIdGet read_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_get(project_id, adapter_id, time_model_id)

Read Time Model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TimeModelsApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
time_model_id = 'time_model_id_example' # str | 

try:
    # Read Time Model
    api_response = api_instance.read_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_get(project_id, adapter_id, time_model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeModelsApi->read_time_model_projects_project_id_adapters_adapter_id_time_models_time_model_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **time_model_id** | **str**|  | 

### Return type

[**ResponseReadTimeModelProjectsProjectIdAdaptersAdapterIdTimeModelsTimeModelIdGet**](ResponseReadTimeModelProjectsProjectIdAdaptersAdapterIdTimeModelsTimeModelIdGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_time_models_projects_project_id_adapters_adapter_id_time_models_get**
> list[object] read_time_models_projects_project_id_adapters_adapter_id_time_models_get(project_id, adapter_id)

Read Time Models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TimeModelsApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Read Time Models
    api_response = api_instance.read_time_models_projects_project_id_adapters_adapter_id_time_models_get(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeModelsApi->read_time_models_projects_project_id_adapters_adapter_id_time_models_get: %s\n" % e)
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

