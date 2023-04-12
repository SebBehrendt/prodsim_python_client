from __future__ import print_function

import json
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

config = swagger_client.Configuration()
config.host = "http://localhost:8000"  # no / at the end


api_client = swagger_client.ApiClient(configuration=config)
# create an instance of the API class
projects_api = swagger_client.ProjectsApi(api_client=api_client)
optimization_api = swagger_client.OptimizationApi(api_client=api_client)


try:
    # Create Example Project
    project = swagger_client.Project(id="Client_Project")
    thread = projects_api.create_project_projects_put(body=project, async_req=True)
    api_response = thread.get()

    print("Created project _________________________________")

    # Load Example Project
    thread = projects_api.load_example_project_load_optimization_example_get(
        async_req=True
    )
    api_response = thread.get()
    pprint(api_response)
    print("Example Project Loaded _________________________________")

    # Get all projects
    thread = projects_api.read_projects_projects_get(async_req=True)
    projects = thread.get()
    pprint(projects)
    print("Example Optimization Project Loaded _________________________________")

    # Load complete production system configuration from JSON file as adapter
    with open("examples/example_configuration.json", "r") as f:
        configuration_data = json.load(f)
    adapter = swagger_client.JsonAdapter(**configuration_data)

    # upload adapter to server
    adapter_api = swagger_client.AdaptersApi(api_client=api_client)
    thread = adapter_api.update_adapter_projects_project_id_adapters_adapter_id_put(
        project_id="Client_Project",
        adapter_id="Client_Adapter",
        body=adapter,
        async_req=True,
    )
    api_response = thread.get()
    print("Created adapter _________________________________")

    # run simulation
    simulation_api = swagger_client.SimulationApi(api_client=api_client)
    thread = simulation_api.run_simulation_projects_project_id_adapters_adapter_id_run_simulation_get(
        project_id="Client_Project", adapter_id="Client_Adapter", async_req=True
    )
    api_response = thread.get()
    print("Simulation finished _________________________________")
    
    # get simulation results
    results_api = swagger_client.ResultsApi(api_client=api_client)
    thread = results_api.get_output_results_projects_project_id_adapters_adapter_id_results_kpi_get(
        project_id="Client_Project", adapter_id="Client_Adapter", kpi=swagger_client.KPIEnum.OUTPUT, async_req=True
    )
    print(f"Configuration had at a simulation time of 3000 minutes an output of: ")
    pprint(thread.get())

    print("Results fetched _________________________________")

    # Add scenario data to adapter by creating contraints, options, info and optimization weights and targets
    constraints = swagger_client.ScenarioConstrainsData(
        max_reconfiguration_cost=100000,
        max_num_machines=8,
        max_num_processes_per_machine=3,
        max_num_transport_resources=3,
        target_material_count={"Material_1": 1000, "Material_2": 1000, "Material_3": 1000} #  only needed for mathematical optimization, target material count in time range
    )
    options = swagger_client.ScenarioOptionsData(
        transformations=[swagger_client.ReconfigurationEnum.LAYOUT, swagger_client.ReconfigurationEnum.SEQUENCING_LOGIC],
        machine_controllers=["FIFO", "SPT", "LIFO"], # has to be added as Enum in server in next api version
        transport_controllers=["FIFO", "SPT_transport"], # has to be added as Enum in server in next api version
        routing_heuristics=["shortest_queue", "random", "FIFO"], # has to be added as Enum in server in next api version
        positions=[ # possible positions for machines
            [0, 0],
            [0, 5],
            [0, 10],
            [0, 15],
            [0, 20],
            [10, 10],
            [10, 15],
            [10, 20],
            [10, 25],
            [20, 10],
            [20, 15],
            [20, 20],
        ] 
    )
    info = swagger_client.ScenarioInfoData(
        machine_cost=20000,
        transport_resource_cost=10000,
        process_module_cost=5000,
        breakdown_cost=0.2, # only for mathematical optimization, minutely cost rate for machines
        maximum_breakdown_time=100, # only for mathematical optimization, allowable time behind schedule because of breakdowns
        time_range=4000 # time range to be considered in optimization in minutes
    )
    scenario_data = swagger_client.ScenarioData(
        constraints=constraints,
        options=options,
        info=info,
        optimize=[swagger_client.KPIEnum.COST, swagger_client.KPIEnum.THROUGHPUT], # KPIs to be optimized. Currently WIP, COST and THROUGHPUT are supported
        weights={ # weights for KPIs in optimization. Only necessary for simulated annealing and tabu search
            swagger_client.KPIEnum.COST: 1,
            swagger_client.KPIEnum.THROUGHPUT: 100,
        }
    )

    # upload scenario data to server
    thread = swagger_client.ScenarioApi(api_client=api_client).create_scenario_projects_project_id_adapters_adapter_id_scenario_put(
        project_id="Client_Project",
        adapter_id="Client_Adapter",
        body=scenario_data,
        async_req=True,
    )
    api_response = thread.get()
    print("Created scenario _________________________________")

    # run optimization for the adapter with the added scenario
    body = swagger_client.SimulatedAnnealingHyperparameters(
        seed=22,
        tmax=10000,
        tmin=1,
        steps=20, # very short run here
        updates=5
    )

    optimization_api = swagger_client.OptimizationApi(api_client=api_client)
    thread = optimization_api.run_configuration_optimization_projects_project_id_adapters_adapter_id_optimize_configuration_post(
        body=body,
        project_id="Client_Project",
        adapter_id="Client_Adapter",
        async_req=True,
    )
    thread.get()
    print("Optimization finished _________________________________")


    # run longer optimization (ca. 10 min) in multiprocessing on the example optimization project
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
    print("Optimization 2 started _________________________________")
    response = thread.get()
    pprint(response)
    print("Optimization 2 finished _________________________________")

    # get optimization core results
    thread = optimization_api.get_optimization_results_projects_project_id_adapters_adapter_id_optimize_configuration_results_get(
        project_id="example_optimization_project", adapter_id="example_adapter_1", async_req=True
    )
    response = thread.get()
    pprint(response)

    print("Optimization results fetched _________________________________")

    # load the pareto optimal solutions from the optimization and register them as adapters in the project

    thread = optimization_api.get_optimization_pareto_front_projects_project_id_adapters_adapter_id_optimize_configuration_pareto_front_performances_get(
        project_id="example_optimization_project", adapter_id="example_adapter_1", async_req=True
    )
    response = thread.get()
    print(response) # list of pareto optimal solutions, which all have been simulated and can be accessed as shown above with their id
    pprint("Pareto Front is registered Finished _________________________________")


except ApiException as e:
    print("Exception when calling ProjectsApi", e)
