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


class Register(object):
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
        'username': 'str',
        'email': 'str',
        'password1': 'str',
        'password2': 'str'
    }

    attribute_map = {
        'username': 'username',
        'email': 'email',
        'password1': 'password1',
        'password2': 'password2'
    }

    def __init__(self, username=None, email=None, password1=None, password2=None, local_vars_configuration=None):  # noqa: E501
        """Register - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._username = None
        self._email = None
        self._password1 = None
        self._password2 = None
        self.discriminator = None

        self.username = username
        self.email = email
        self.password1 = password1
        self.password2 = password2

    @property
    def username(self):
        """Gets the username of this Register.  # noqa: E501


        :return: The username of this Register.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Register.


        :param username: The username of this Register.  # noqa: E501
        :type username: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) > 150):
            raise ValueError("Invalid value for `username`, length must be less than or equal to `150`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) < 1):
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

    @property
    def email(self):
        """Gets the email of this Register.  # noqa: E501


        :return: The email of this Register.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Register.


        :param email: The email of this Register.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def password1(self):
        """Gets the password1 of this Register.  # noqa: E501


        :return: The password1 of this Register.  # noqa: E501
        :rtype: str
        """
        return self._password1

    @password1.setter
    def password1(self, password1):
        """Sets the password1 of this Register.


        :param password1: The password1 of this Register.  # noqa: E501
        :type password1: str
        """
        if self.local_vars_configuration.client_side_validation and password1 is None:  # noqa: E501
            raise ValueError("Invalid value for `password1`, must not be `None`")  # noqa: E501

        self._password1 = password1

    @property
    def password2(self):
        """Gets the password2 of this Register.  # noqa: E501


        :return: The password2 of this Register.  # noqa: E501
        :rtype: str
        """
        return self._password2

    @password2.setter
    def password2(self, password2):
        """Sets the password2 of this Register.


        :param password2: The password2 of this Register.  # noqa: E501
        :type password2: str
        """
        if self.local_vars_configuration.client_side_validation and password2 is None:  # noqa: E501
            raise ValueError("Invalid value for `password2`, must not be `None`")  # noqa: E501

        self._password2 = password2

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
        if not isinstance(other, Register):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Register):
            return True

        return self.to_dict() != other.to_dict()