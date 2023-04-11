# swagger_client.ProjectsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_projects_put**](ProjectsApi.md#create_project_projects_put) | **PUT** /projects | Create Project
[**delete_project_projects_project_id_delete**](ProjectsApi.md#delete_project_projects_project_id_delete) | **DELETE** /projects/{project_id} | Delete Project
[**load_example_project_load_example_project_get**](ProjectsApi.md#load_example_project_load_example_project_get) | **GET** /load_example_project | Load Example Project
[**load_example_project_load_optimization_example_get**](ProjectsApi.md#load_example_project_load_optimization_example_get) | **GET** /load_optimization_example | Load Example Project
[**read_project_projects_project_id_get**](ProjectsApi.md#read_project_projects_project_id_get) | **GET** /projects/{project_id} | Read Project
[**read_projects_projects_get**](ProjectsApi.md#read_projects_projects_get) | **GET** /projects | Read Projects

# **create_project_projects_put**
> object create_project_projects_put(body)

Create Project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
body = swagger_client.Project() # Project | 

try:
    # Create Project
    api_response = api_instance.create_project_projects_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project_projects_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Project**](Project.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_projects_project_id_delete**
> object delete_project_projects_project_id_delete(project_id)

Delete Project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 'project_id_example' # str | 

try:
    # Delete Project
    api_response = api_instance.delete_project_projects_project_id_delete(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_project_projects_project_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_example_project_load_example_project_get**
> str load_example_project_load_example_project_get()

Load Example Project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()

try:
    # Load Example Project
    api_response = api_instance.load_example_project_load_example_project_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->load_example_project_load_example_project_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_example_project_load_optimization_example_get**
> str load_example_project_load_optimization_example_get()

Load Example Project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()

try:
    # Load Example Project
    api_response = api_instance.load_example_project_load_optimization_example_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->load_example_project_load_optimization_example_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_project_projects_project_id_get**
> Project read_project_projects_project_id_get(project_id)

Read Project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 'project_id_example' # str | 

try:
    # Read Project
    api_response = api_instance.read_project_projects_project_id_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->read_project_projects_project_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_projects_projects_get**
> list[Project] read_projects_projects_get()

Read Projects

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()

try:
    # Read Projects
    api_response = api_instance.read_projects_projects_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->read_projects_projects_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

