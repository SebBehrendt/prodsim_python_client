# swagger_client.MaterialsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_material_projects_project_id_adapters_adapter_id_materials_material_id_put**](MaterialsApi.md#create_material_projects_project_id_adapters_adapter_id_materials_material_id_put) | **PUT** /projects/{project_id}/adapters/{adapter_id}/materials/{material_id} | Create Material
[**read_material_projects_project_id_adapters_adapter_id_materials_material_id_get**](MaterialsApi.md#read_material_projects_project_id_adapters_adapter_id_materials_material_id_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/materials/{material_id} | Read Material
[**read_materials_projects_project_id_adapters_adapter_id_materials_get**](MaterialsApi.md#read_materials_projects_project_id_adapters_adapter_id_materials_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/materials | Read Materials

# **create_material_projects_project_id_adapters_adapter_id_materials_material_id_put**
> object create_material_projects_project_id_adapters_adapter_id_materials_material_id_put(body, project_id, adapter_id, material_id)

Create Material

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialsApi()
body = swagger_client.MaterialData() # MaterialData | 
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
material_id = NULL # object | 

try:
    # Create Material
    api_response = api_instance.create_material_projects_project_id_adapters_adapter_id_materials_material_id_put(body, project_id, adapter_id, material_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialsApi->create_material_projects_project_id_adapters_adapter_id_materials_material_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaterialData**](MaterialData.md)|  | 
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **material_id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_material_projects_project_id_adapters_adapter_id_materials_material_id_get**
> MaterialData read_material_projects_project_id_adapters_adapter_id_materials_material_id_get(project_id, adapter_id, material_id)

Read Material

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialsApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
material_id = 'material_id_example' # str | 

try:
    # Read Material
    api_response = api_instance.read_material_projects_project_id_adapters_adapter_id_materials_material_id_get(project_id, adapter_id, material_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialsApi->read_material_projects_project_id_adapters_adapter_id_materials_material_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **material_id** | **str**|  | 

### Return type

[**MaterialData**](MaterialData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_materials_projects_project_id_adapters_adapter_id_materials_get**
> list[MaterialData] read_materials_projects_project_id_adapters_adapter_id_materials_get(project_id, adapter_id)

Read Materials

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaterialsApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Read Materials
    api_response = api_instance.read_materials_projects_project_id_adapters_adapter_id_materials_get(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaterialsApi->read_materials_projects_project_id_adapters_adapter_id_materials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

[**list[MaterialData]**](MaterialData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

