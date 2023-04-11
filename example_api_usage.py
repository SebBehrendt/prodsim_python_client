from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

config = swagger_client.Configuration()
config.host = "http://localhost:8000"
api_client = swagger_client.ApiClient(configuration=config)
# create an instance of the API class
api_instance = swagger_client.ProjectsApi(api_client=api_client)
optimization_api = swagger_client.OptimizationApi(api_client=api_client)


try:
    # Load Example Project
    api_response = api_instance.load_example_project_load_example_project_get()
    pprint(api_response)
    projects = api_instance.read_projects_projects_get()
    pprint(projects)
    hyperparams = swagger_client.EvolutionaryAlgorithmHyperparameters(seed=22, number_of_generations=32, population_size=128, mutation_rate=0.15, crossover_rate=0.1, number_of_processes=8)

    response = optimization_api.run_configuration_optimization_projects_project_id_adapters_adapter_id_optimize_configuration_post(
        body=hyperparams, project_id="example_optimization_project", adapter_id="example_adapter_1")
    pprint(response)
    response = optimization_api.get_optimization_pareto_front_projects_project_id_adapters_adapter_id_optimize_configuration_pareto_front_performances_get(
        project_id="example_optimization_project", adapter_id="example_adapter_1")
    
    

except ApiException as e:
    print("Exception when calling ProjectsApi->load_example_project_load_example_project_get: %s\n" % e)