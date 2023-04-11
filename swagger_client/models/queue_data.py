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

class QueueData(object):
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
        'id': 'str',
        'description': 'str',
        'capacity': 'AnyOfQueueDataCapacity'
    }

    attribute_map = {
        'id': 'ID',
        'description': 'description',
        'capacity': 'capacity'
    }

    def __init__(self, id=None, description=None, capacity=None):  # noqa: E501
        """QueueData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._description = None
        self._capacity = None
        self.discriminator = None
        self.id = id
        self.description = description
        if capacity is not None:
            self.capacity = capacity

    @property
    def id(self):
        """Gets the id of this QueueData.  # noqa: E501


        :return: The id of this QueueData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueueData.


        :param id: The id of this QueueData.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def description(self):
        """Gets the description of this QueueData.  # noqa: E501


        :return: The description of this QueueData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueueData.


        :param description: The description of this QueueData.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def capacity(self):
        """Gets the capacity of this QueueData.  # noqa: E501


        :return: The capacity of this QueueData.  # noqa: E501
        :rtype: AnyOfQueueDataCapacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this QueueData.


        :param capacity: The capacity of this QueueData.  # noqa: E501
        :type: AnyOfQueueDataCapacity
        """

        self._capacity = capacity

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
        if issubclass(QueueData, dict):
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
        if not isinstance(other, QueueData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other