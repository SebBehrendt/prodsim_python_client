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

class MathOptHyperparameters(object):
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
        'optimization_time_portion': 'float',
        'number_of_solutions': 'int',
        'adjusted_number_of_transport_resources': 'int'
    }

    attribute_map = {
        'optimization_time_portion': 'optimization_time_portion',
        'number_of_solutions': 'number_of_solutions',
        'adjusted_number_of_transport_resources': 'adjusted_number_of_transport_resources'
    }

    def __init__(self, optimization_time_portion=0.5, number_of_solutions=1, adjusted_number_of_transport_resources=1):  # noqa: E501
        """MathOptHyperparameters - a model defined in Swagger"""  # noqa: E501
        self._optimization_time_portion = None
        self._number_of_solutions = None
        self._adjusted_number_of_transport_resources = None
        self.discriminator = None
        if optimization_time_portion is not None:
            self.optimization_time_portion = optimization_time_portion
        if number_of_solutions is not None:
            self.number_of_solutions = number_of_solutions
        if adjusted_number_of_transport_resources is not None:
            self.adjusted_number_of_transport_resources = adjusted_number_of_transport_resources

    @property
    def optimization_time_portion(self):
        """Gets the optimization_time_portion of this MathOptHyperparameters.  # noqa: E501

        Portion of the total time that is used for optimization.  # noqa: E501

        :return: The optimization_time_portion of this MathOptHyperparameters.  # noqa: E501
        :rtype: float
        """
        return self._optimization_time_portion

    @optimization_time_portion.setter
    def optimization_time_portion(self, optimization_time_portion):
        """Sets the optimization_time_portion of this MathOptHyperparameters.

        Portion of the total time that is used for optimization.  # noqa: E501

        :param optimization_time_portion: The optimization_time_portion of this MathOptHyperparameters.  # noqa: E501
        :type: float
        """

        self._optimization_time_portion = optimization_time_portion

    @property
    def number_of_solutions(self):
        """Gets the number_of_solutions of this MathOptHyperparameters.  # noqa: E501

        Number of solutions that are generated.  # noqa: E501

        :return: The number_of_solutions of this MathOptHyperparameters.  # noqa: E501
        :rtype: int
        """
        return self._number_of_solutions

    @number_of_solutions.setter
    def number_of_solutions(self, number_of_solutions):
        """Sets the number_of_solutions of this MathOptHyperparameters.

        Number of solutions that are generated.  # noqa: E501

        :param number_of_solutions: The number_of_solutions of this MathOptHyperparameters.  # noqa: E501
        :type: int
        """

        self._number_of_solutions = number_of_solutions

    @property
    def adjusted_number_of_transport_resources(self):
        """Gets the adjusted_number_of_transport_resources of this MathOptHyperparameters.  # noqa: E501

        Number of transport resources that are used for the optimization.  # noqa: E501

        :return: The adjusted_number_of_transport_resources of this MathOptHyperparameters.  # noqa: E501
        :rtype: int
        """
        return self._adjusted_number_of_transport_resources

    @adjusted_number_of_transport_resources.setter
    def adjusted_number_of_transport_resources(self, adjusted_number_of_transport_resources):
        """Sets the adjusted_number_of_transport_resources of this MathOptHyperparameters.

        Number of transport resources that are used for the optimization.  # noqa: E501

        :param adjusted_number_of_transport_resources: The adjusted_number_of_transport_resources of this MathOptHyperparameters.  # noqa: E501
        :type: int
        """

        self._adjusted_number_of_transport_resources = adjusted_number_of_transport_resources

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
        if issubclass(MathOptHyperparameters, dict):
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
        if not isinstance(other, MathOptHyperparameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
