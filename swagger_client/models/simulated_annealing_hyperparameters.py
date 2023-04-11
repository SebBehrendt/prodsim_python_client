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

class SimulatedAnnealingHyperparameters(object):
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
        'seed': 'int',
        'tmax': 'int',
        'tmin': 'int',
        'steps': 'int',
        'updates': 'int'
    }

    attribute_map = {
        'seed': 'seed',
        'tmax': 'Tmax',
        'tmin': 'Tmin',
        'steps': 'steps',
        'updates': 'updates'
    }

    def __init__(self, seed=0, tmax=10000, tmin=1, steps=4000, updates=300):  # noqa: E501
        """SimulatedAnnealingHyperparameters - a model defined in Swagger"""  # noqa: E501
        self._seed = None
        self._tmax = None
        self._tmin = None
        self._steps = None
        self._updates = None
        self.discriminator = None
        if seed is not None:
            self.seed = seed
        if tmax is not None:
            self.tmax = tmax
        if tmin is not None:
            self.tmin = tmin
        if steps is not None:
            self.steps = steps
        if updates is not None:
            self.updates = updates

    @property
    def seed(self):
        """Gets the seed of this SimulatedAnnealingHyperparameters.  # noqa: E501

        Seed for random number generator  # noqa: E501

        :return: The seed of this SimulatedAnnealingHyperparameters.  # noqa: E501
        :rtype: int
        """
        return self._seed

    @seed.setter
    def seed(self, seed):
        """Sets the seed of this SimulatedAnnealingHyperparameters.

        Seed for random number generator  # noqa: E501

        :param seed: The seed of this SimulatedAnnealingHyperparameters.  # noqa: E501
        :type: int
        """

        self._seed = seed

    @property
    def tmax(self):
        """Gets the tmax of this SimulatedAnnealingHyperparameters.  # noqa: E501

        Maximum temperature  # noqa: E501

        :return: The tmax of this SimulatedAnnealingHyperparameters.  # noqa: E501
        :rtype: int
        """
        return self._tmax

    @tmax.setter
    def tmax(self, tmax):
        """Sets the tmax of this SimulatedAnnealingHyperparameters.

        Maximum temperature  # noqa: E501

        :param tmax: The tmax of this SimulatedAnnealingHyperparameters.  # noqa: E501
        :type: int
        """

        self._tmax = tmax

    @property
    def tmin(self):
        """Gets the tmin of this SimulatedAnnealingHyperparameters.  # noqa: E501

        Minimum temperature  # noqa: E501

        :return: The tmin of this SimulatedAnnealingHyperparameters.  # noqa: E501
        :rtype: int
        """
        return self._tmin

    @tmin.setter
    def tmin(self, tmin):
        """Sets the tmin of this SimulatedAnnealingHyperparameters.

        Minimum temperature  # noqa: E501

        :param tmin: The tmin of this SimulatedAnnealingHyperparameters.  # noqa: E501
        :type: int
        """

        self._tmin = tmin

    @property
    def steps(self):
        """Gets the steps of this SimulatedAnnealingHyperparameters.  # noqa: E501

        Number of steps  # noqa: E501

        :return: The steps of this SimulatedAnnealingHyperparameters.  # noqa: E501
        :rtype: int
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this SimulatedAnnealingHyperparameters.

        Number of steps  # noqa: E501

        :param steps: The steps of this SimulatedAnnealingHyperparameters.  # noqa: E501
        :type: int
        """

        self._steps = steps

    @property
    def updates(self):
        """Gets the updates of this SimulatedAnnealingHyperparameters.  # noqa: E501

        Number of updates  # noqa: E501

        :return: The updates of this SimulatedAnnealingHyperparameters.  # noqa: E501
        :rtype: int
        """
        return self._updates

    @updates.setter
    def updates(self, updates):
        """Sets the updates of this SimulatedAnnealingHyperparameters.

        Number of updates  # noqa: E501

        :param updates: The updates of this SimulatedAnnealingHyperparameters.  # noqa: E501
        :type: int
        """

        self._updates = updates

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
        if issubclass(SimulatedAnnealingHyperparameters, dict):
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
        if not isinstance(other, SimulatedAnnealingHyperparameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other