# swagger_client.OptimizationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_optimization_pareto_front_projects_project_id_adapters_adapter_id_optimize_configuration_pareto_front_performances_get**](OptimizationApi.md#get_optimization_pareto_front_projects_project_id_adapters_adapter_id_optimize_configuration_pareto_front_performances_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/optimize_configuration/pareto_front_performances | Get Optimization Pareto Front
[**get_optimization_results_projects_project_id_adapters_adapter_id_optimize_configuration_results_get**](OptimizationApi.md#get_optimization_results_projects_project_id_adapters_adapter_id_optimize_configuration_results_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/optimize_configuration/results | Get Optimization Results
[**get_optimization_solution_projects_project_id_adapters_adapter_id_optimize_configuration_solution_id_get**](OptimizationApi.md#get_optimization_solution_projects_project_id_adapters_adapter_id_optimize_configuration_solution_id_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/optimize_configuration/{solution_id} | Get Optimization Solution
[**register_adapter_with_evaluation_projects_project_id_adapters_adapter_id_optimize_configuration_register_solution_id_get**](OptimizationApi.md#register_adapter_with_evaluation_projects_project_id_adapters_adapter_id_optimize_configuration_register_solution_id_get) | **GET** /projects/{project_id}/adapters/{adapter_id}/optimize_configuration/register/{solution_id} | Register Adapter With Evaluation
[**run_configuration_optimization_projects_project_id_adapters_adapter_id_optimize_configuration_post**](OptimizationApi.md#run_configuration_optimization_projects_project_id_adapters_adapter_id_optimize_configuration_post) | **POST** /projects/{project_id}/adapters/{adapter_id}/optimize_configuration | Run Configuration Optimization

# **get_optimization_pareto_front_projects_project_id_adapters_adapter_id_optimize_configuration_pareto_front_performances_get**
> str get_optimization_pareto_front_projects_project_id_adapters_adapter_id_optimize_configuration_pareto_front_performances_get(project_id, adapter_id)

Get Optimization Pareto Front

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OptimizationApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Get Optimization Pareto Front
    api_response = api_instance.get_optimization_pareto_front_projects_project_id_adapters_adapter_id_optimize_configuration_pareto_front_performances_get(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptimizationApi->get_optimization_pareto_front_projects_project_id_adapters_adapter_id_optimize_configuration_pareto_front_performances_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_optimization_results_projects_project_id_adapters_adapter_id_optimize_configuration_results_get**
> dict(str, list[object]) get_optimization_results_projects_project_id_adapters_adapter_id_optimize_configuration_results_get(project_id, adapter_id)

Get Optimization Results

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OptimizationApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Get Optimization Results
    api_response = api_instance.get_optimization_results_projects_project_id_adapters_adapter_id_optimize_configuration_results_get(project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptimizationApi->get_optimization_results_projects_project_id_adapters_adapter_id_optimize_configuration_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

**dict(str, list[object])**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_optimization_solution_projects_project_id_adapters_adapter_id_optimize_configuration_solution_id_get**
> JsonAdapter get_optimization_solution_projects_project_id_adapters_adapter_id_optimize_configuration_solution_id_get(project_id, adapter_id, solution_id)

Get Optimization Solution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OptimizationApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
solution_id = 'solution_id_example' # str | 

try:
    # Get Optimization Solution
    api_response = api_instance.get_optimization_solution_projects_project_id_adapters_adapter_id_optimize_configuration_solution_id_get(project_id, adapter_id, solution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptimizationApi->get_optimization_solution_projects_project_id_adapters_adapter_id_optimize_configuration_solution_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **solution_id** | **str**|  | 

### Return type

[**JsonAdapter**](JsonAdapter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_adapter_with_evaluation_projects_project_id_adapters_adapter_id_optimize_configuration_register_solution_id_get**
> str register_adapter_with_evaluation_projects_project_id_adapters_adapter_id_optimize_configuration_register_solution_id_get(project_id, adapter_id, solution_id)

Register Adapter With Evaluation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OptimizationApi()
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 
solution_id = 'solution_id_example' # str | 

try:
    # Register Adapter With Evaluation
    api_response = api_instance.register_adapter_with_evaluation_projects_project_id_adapters_adapter_id_optimize_configuration_register_solution_id_get(project_id, adapter_id, solution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptimizationApi->register_adapter_with_evaluation_projects_project_id_adapters_adapter_id_optimize_configuration_register_solution_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 
 **solution_id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_configuration_optimization_projects_project_id_adapters_adapter_id_optimize_configuration_post**
> str run_configuration_optimization_projects_project_id_adapters_adapter_id_optimize_configuration_post(body, project_id, adapter_id)

Run Configuration Optimization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OptimizationApi()
body = swagger_client.HyperParameters() # HyperParameters | 
project_id = 'project_id_example' # str | 
adapter_id = 'adapter_id_example' # str | 

try:
    # Run Configuration Optimization
    api_response = api_instance.run_configuration_optimization_projects_project_id_adapters_adapter_id_optimize_configuration_post(body, project_id, adapter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptimizationApi->run_configuration_optimization_projects_project_id_adapters_adapter_id_optimize_configuration_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HyperParameters**](HyperParameters.md)|  | 
 **project_id** | **str**|  | 
 **adapter_id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

