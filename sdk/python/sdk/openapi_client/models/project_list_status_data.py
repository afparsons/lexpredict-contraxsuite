# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ProjectListStatusData(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'name': 'str',
        'code': 'str',
        'order': 'int',
        'is_active': 'bool',
        'group': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'code': 'code',
        'order': 'order',
        'is_active': 'is_active',
        'group': 'group'
    }

    def __init__(self, id=None, name=None, code=None, order=None, is_active=None, group=None, local_vars_configuration=None):  # noqa: E501
        """ProjectListStatusData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._code = None
        self._order = None
        self._is_active = None
        self._group = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.code = code
        self.order = order
        if is_active is not None:
            self.is_active = is_active
        self.group = group

    @property
    def id(self):
        """Gets the id of this ProjectListStatusData.  # noqa: E501


        :return: The id of this ProjectListStatusData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectListStatusData.


        :param id: The id of this ProjectListStatusData.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProjectListStatusData.  # noqa: E501


        :return: The name of this ProjectListStatusData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectListStatusData.


        :param name: The name of this ProjectListStatusData.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501

        self._name = name

    @property
    def code(self):
        """Gets the code of this ProjectListStatusData.  # noqa: E501


        :return: The code of this ProjectListStatusData.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ProjectListStatusData.


        :param code: The code of this ProjectListStatusData.  # noqa: E501
        :type code: str
        """
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 100):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `100`")  # noqa: E501

        self._code = code

    @property
    def order(self):
        """Gets the order of this ProjectListStatusData.  # noqa: E501


        :return: The order of this ProjectListStatusData.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ProjectListStatusData.


        :param order: The order of this ProjectListStatusData.  # noqa: E501
        :type order: int
        """
        if self.local_vars_configuration.client_side_validation and order is None:  # noqa: E501
            raise ValueError("Invalid value for `order`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                order is not None and order > 32767):  # noqa: E501
            raise ValueError("Invalid value for `order`, must be a value less than or equal to `32767`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                order is not None and order < 0):  # noqa: E501
            raise ValueError("Invalid value for `order`, must be a value greater than or equal to `0`")  # noqa: E501

        self._order = order

    @property
    def is_active(self):
        """Gets the is_active of this ProjectListStatusData.  # noqa: E501


        :return: The is_active of this ProjectListStatusData.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this ProjectListStatusData.


        :param is_active: The is_active of this ProjectListStatusData.  # noqa: E501
        :type is_active: bool
        """

        self._is_active = is_active

    @property
    def group(self):
        """Gets the group of this ProjectListStatusData.  # noqa: E501


        :return: The group of this ProjectListStatusData.  # noqa: E501
        :rtype: int
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ProjectListStatusData.


        :param group: The group of this ProjectListStatusData.  # noqa: E501
        :type group: int
        """

        self._group = group

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProjectListStatusData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectListStatusData):
            return True

        return self.to_dict() != other.to_dict()