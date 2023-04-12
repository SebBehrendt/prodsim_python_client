from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

config = swagger_client.Configuration()
config.host = "http://localhost:8000"  # no / at the end


api_client = swagger_client.ApiClient(configuration=config)
# create an instance of the API class
api_instance = swagger_client.ProjectsApi(api_client=api_client)
optimization_api = swagger_client.OptimizationApi(api_client=api_client)


try:
    # Load Example Project
    thread = api_instance.load_example_project_load_optimization_example_get(async_req=True)
    api_response = thread.get()
    pprint(api_response)

    pprint("Example Project Loaded _________________________________")

    thread = api_instance.read_projects_projects_get(async_req=True)
    projects = thread.get()
    pprint(projects)
    pprint("Example Optimization Project Loaded _________________________________")

    hyperparams = swagger_client.EvolutionaryAlgorithmHyperparameters(
        seed=22,
        number_of_generations=32,
        population_size=128,
        mutation_rate=0.15,
        crossover_rate=0.1,
        number_of_processes=8,
    )
    thread = optimization_api.run_configuration_optimization_projects_project_id_adapters_adapter_id_optimize_configuration_post(
        body=hyperparams,
        project_id="example_optimization_project",
        adapter_id="example_adapter_1",
        async_req=True,
    )
    response = thread.get()
    pprint(response)
    pprint("Optimization Started _________________________________")

    thread = optimization_api.get_optimization_pareto_front_projects_project_id_adapters_adapter_id_optimize_configuration_pareto_front_performances_get(
        project_id="example_optimization_project", adapter_id="example_adapter_1", async_req=True
    )
    response = thread.get()
    pprint(response)
    pprint("Optimization Finished _________________________________")


except ApiException as e:
    print("Exception when calling ProjectsApi", e)
