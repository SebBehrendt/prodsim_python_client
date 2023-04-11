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

class UnscheduledDowntime(object):
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
        'name': 'str',
        'target': 'str',
        'weight': 'float',
        'value': 'float',
        'context': 'list[KPILevelEnum]',
        'resource': 'str',
        'material_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'target': 'target',
        'weight': 'weight',
        'value': 'value',
        'context': 'context',
        'resource': 'resource',
        'material_type': 'material_type'
    }

    def __init__(self, name=None, target='min', weight=1, value=None, context=None, resource=None, material_type=None):  # noqa: E501
        """UnscheduledDowntime - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._target = None
        self._weight = None
        self._value = None
        self._context = None
        self._resource = None
        self._material_type = None
        self.discriminator = None
        self.name = name
        if target is not None:
            self.target = target
        if weight is not None:
            self.weight = weight
        if value is not None:
            self.value = value
        if context is not None:
            self.context = context
        if resource is not None:
            self.resource = resource
        if material_type is not None:
            self.material_type = material_type

    @property
    def name(self):
        """Gets the name of this UnscheduledDowntime.  # noqa: E501


        :return: The name of this UnscheduledDowntime.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UnscheduledDowntime.


        :param name: The name of this UnscheduledDowntime.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        allowed_values = ["unscheduled_downtime"]  # noqa: E501
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def target(self):
        """Gets the target of this UnscheduledDowntime.  # noqa: E501


        :return: The target of this UnscheduledDowntime.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this UnscheduledDowntime.


        :param target: The target of this UnscheduledDowntime.  # noqa: E501
        :type: str
        """
        allowed_values = ["min"]  # noqa: E501
        if target not in allowed_values:
            raise ValueError(
                "Invalid value for `target` ({0}), must be one of {1}"  # noqa: E501
                .format(target, allowed_values)
            )

        self._target = target

    @property
    def weight(self):
        """Gets the weight of this UnscheduledDowntime.  # noqa: E501


        :return: The weight of this UnscheduledDowntime.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this UnscheduledDowntime.


        :param weight: The weight of this UnscheduledDowntime.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def value(self):
        """Gets the value of this UnscheduledDowntime.  # noqa: E501


        :return: The value of this UnscheduledDowntime.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UnscheduledDowntime.


        :param value: The value of this UnscheduledDowntime.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def context(self):
        """Gets the context of this UnscheduledDowntime.  # noqa: E501


        :return: The context of this UnscheduledDowntime.  # noqa: E501
        :rtype: list[KPILevelEnum]
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this UnscheduledDowntime.


        :param context: The context of this UnscheduledDowntime.  # noqa: E501
        :type: list[KPILevelEnum]
        """

        self._context = context

    @property
    def resource(self):
        """Gets the resource of this UnscheduledDowntime.  # noqa: E501


        :return: The resource of this UnscheduledDowntime.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this UnscheduledDowntime.


        :param resource: The resource of this UnscheduledDowntime.  # noqa: E501
        :type: str
        """

        self._resource = resource

    @property
    def material_type(self):
        """Gets the material_type of this UnscheduledDowntime.  # noqa: E501


        :return: The material_type of this UnscheduledDowntime.  # noqa: E501
        :rtype: str
        """
        return self._material_type

    @material_type.setter
    def material_type(self, material_type):
        """Sets the material_type of this UnscheduledDowntime.


        :param material_type: The material_type of this UnscheduledDowntime.  # noqa: E501
        :type: str
        """

        self._material_type = material_type

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
        if issubclass(UnscheduledDowntime, dict):
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
        if not isinstance(other, UnscheduledDowntime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
