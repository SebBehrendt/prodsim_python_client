# coding: utf-8

"""
    ProdSim API

     The ProdSim-API allows you to create and run production simulations and optimizations with the ProdSim library.    # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: sebastianbehrendt97@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ScenarioConstrainsData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'max_reconfiguration_cost': 'float',
        'max_num_machines': 'int',
        'max_num_processes_per_machine': 'int',
        'max_num_transport_resources': 'int',
        'target_material_count': 'dict(str, int)'
    }

    attribute_map = {
        'max_reconfiguration_cost': 'max_reconfiguration_cost',
        'max_num_machines': 'max_num_machines',
        'max_num_processes_per_machine': 'max_num_processes_per_machine',
        'max_num_transport_resources': 'max_num_transport_resources',
        'target_material_count': 'target_material_count'
    }

    def __init__(self, max_reconfiguration_cost=None, max_num_machines=None, max_num_processes_per_machine=None, max_num_transport_resources=None, target_material_count=None):  # noqa: E501
        """ScenarioConstrainsData - a model defined in Swagger"""  # noqa: E501
        self._max_reconfiguration_cost = None
        self._max_num_machines = None
        self._max_num_processes_per_machine = None
        self._max_num_transport_resources = None
        self._target_material_count = None
        self.discriminator = None
        self.max_reconfiguration_cost = max_reconfiguration_cost
        self.max_num_machines = max_num_machines
        self.max_num_processes_per_machine = max_num_processes_per_machine
        self.max_num_transport_resources = max_num_transport_resources
        if target_material_count is not None:
            self.target_material_count = target_material_count

    @property
    def max_reconfiguration_cost(self):
        """Gets the max_reconfiguration_cost of this ScenarioConstrainsData.  # noqa: E501


        :return: The max_reconfiguration_cost of this ScenarioConstrainsData.  # noqa: E501
        :rtype: float
        """
        return self._max_reconfiguration_cost

    @max_reconfiguration_cost.setter
    def max_reconfiguration_cost(self, max_reconfiguration_cost):
        """Sets the max_reconfiguration_cost of this ScenarioConstrainsData.


        :param max_reconfiguration_cost: The max_reconfiguration_cost of this ScenarioConstrainsData.  # noqa: E501
        :type: float
        """
        if max_reconfiguration_cost is None:
            raise ValueError("Invalid value for `max_reconfiguration_cost`, must not be `None`")  # noqa: E501

        self._max_reconfiguration_cost = max_reconfiguration_cost

    @property
    def max_num_machines(self):
        """Gets the max_num_machines of this ScenarioConstrainsData.  # noqa: E501


        :return: The max_num_machines of this ScenarioConstrainsData.  # noqa: E501
        :rtype: int
        """
        return self._max_num_machines

    @max_num_machines.setter
    def max_num_machines(self, max_num_machines):
        """Sets the max_num_machines of this ScenarioConstrainsData.


        :param max_num_machines: The max_num_machines of this ScenarioConstrainsData.  # noqa: E501
        :type: int
        """
        if max_num_machines is None:
            raise ValueError("Invalid value for `max_num_machines`, must not be `None`")  # noqa: E501

        self._max_num_machines = max_num_machines

    @property
    def max_num_processes_per_machine(self):
        """Gets the max_num_processes_per_machine of this ScenarioConstrainsData.  # noqa: E501


        :return: The max_num_processes_per_machine of this ScenarioConstrainsData.  # noqa: E501
        :rtype: int
        """
        return self._max_num_processes_per_machine

    @max_num_processes_per_machine.setter
    def max_num_processes_per_machine(self, max_num_processes_per_machine):
        """Sets the max_num_processes_per_machine of this ScenarioConstrainsData.


        :param max_num_processes_per_machine: The max_num_processes_per_machine of this ScenarioConstrainsData.  # noqa: E501
        :type: int
        """
        if max_num_processes_per_machine is None:
            raise ValueError("Invalid value for `max_num_processes_per_machine`, must not be `None`")  # noqa: E501

        self._max_num_processes_per_machine = max_num_processes_per_machine

    @property
    def max_num_transport_resources(self):
        """Gets the max_num_transport_resources of this ScenarioConstrainsData.  # noqa: E501


        :return: The max_num_transport_resources of this ScenarioConstrainsData.  # noqa: E501
        :rtype: int
        """
        return self._max_num_transport_resources

    @max_num_transport_resources.setter
    def max_num_transport_resources(self, max_num_transport_resources):
        """Sets the max_num_transport_resources of this ScenarioConstrainsData.


        :param max_num_transport_resources: The max_num_transport_resources of this ScenarioConstrainsData.  # noqa: E501
        :type: int
        """
        if max_num_transport_resources is None:
            raise ValueError("Invalid value for `max_num_transport_resources`, must not be `None`")  # noqa: E501

        self._max_num_transport_resources = max_num_transport_resources

    @property
    def target_material_count(self):
        """Gets the target_material_count of this ScenarioConstrainsData.  # noqa: E501


        :return: The target_material_count of this ScenarioConstrainsData.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._target_material_count

    @target_material_count.setter
    def target_material_count(self, target_material_count):
        """Sets the target_material_count of this ScenarioConstrainsData.


        :param target_material_count: The target_material_count of this ScenarioConstrainsData.  # noqa: E501
        :type: dict(str, int)
        """

        self._target_material_count = target_material_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ScenarioConstrainsData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScenarioConstrainsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
