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


class TextUnitClassifierSuggestion(object):
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
        'pk': 'int',
        'text_unit__document__pk': 'str',
        'text_unit__document__name': 'str',
        'text_unit__document__document_type': 'str',
        'text_unit__document__description': 'str',
        'text_unit__pk': 'str',
        'class_name': 'str',
        'class_value': 'str',
        'classifier_run': 'datetime',
        'classifier_confidence': 'float'
    }

    attribute_map = {
        'pk': 'pk',
        'text_unit__document__pk': 'text_unit__document__pk',
        'text_unit__document__name': 'text_unit__document__name',
        'text_unit__document__document_type': 'text_unit__document__document_type',
        'text_unit__document__description': 'text_unit__document__description',
        'text_unit__pk': 'text_unit__pk',
        'class_name': 'class_name',
        'class_value': 'class_value',
        'classifier_run': 'classifier_run',
        'classifier_confidence': 'classifier_confidence'
    }

    def __init__(self, pk=None, text_unit__document__pk=None, text_unit__document__name=None, text_unit__document__document_type=None, text_unit__document__description=None, text_unit__pk=None, class_name=None, class_value=None, classifier_run=None, classifier_confidence=None, local_vars_configuration=None):  # noqa: E501
        """TextUnitClassifierSuggestion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pk = None
        self._text_unit__document__pk = None
        self._text_unit__document__name = None
        self._text_unit__document__document_type = None
        self._text_unit__document__description = None
        self._text_unit__pk = None
        self._class_name = None
        self._class_value = None
        self._classifier_run = None
        self._classifier_confidence = None
        self.discriminator = None

        if pk is not None:
            self.pk = pk
        if text_unit__document__pk is not None:
            self.text_unit__document__pk = text_unit__document__pk
        if text_unit__document__name is not None:
            self.text_unit__document__name = text_unit__document__name
        if text_unit__document__document_type is not None:
            self.text_unit__document__document_type = text_unit__document__document_type
        if text_unit__document__description is not None:
            self.text_unit__document__description = text_unit__document__description
        if text_unit__pk is not None:
            self.text_unit__pk = text_unit__pk
        self.class_name = class_name
        self.class_value = class_value
        if classifier_run is not None:
            self.classifier_run = classifier_run
        if classifier_confidence is not None:
            self.classifier_confidence = classifier_confidence

    @property
    def pk(self):
        """Gets the pk of this TextUnitClassifierSuggestion.  # noqa: E501


        :return: The pk of this TextUnitClassifierSuggestion.  # noqa: E501
        :rtype: int
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this TextUnitClassifierSuggestion.


        :param pk: The pk of this TextUnitClassifierSuggestion.  # noqa: E501
        :type pk: int
        """

        self._pk = pk

    @property
    def text_unit__document__pk(self):
        """Gets the text_unit__document__pk of this TextUnitClassifierSuggestion.  # noqa: E501


        :return: The text_unit__document__pk of this TextUnitClassifierSuggestion.  # noqa: E501
        :rtype: str
        """
        return self._text_unit__document__pk

    @text_unit__document__pk.setter
    def text_unit__document__pk(self, text_unit__document__pk):
        """Sets the text_unit__document__pk of this TextUnitClassifierSuggestion.


        :param text_unit__document__pk: The text_unit__document__pk of this TextUnitClassifierSuggestion.  # noqa: E501
        :type text_unit__document__pk: str
        """

        self._text_unit__document__pk = text_unit__document__pk

    @property
    def text_unit__document__name(self):
        """Gets the text_unit__document__name of this TextUnitClassifierSuggestion.  # noqa: E501


        :return: The text_unit__document__name of this TextUnitClassifierSuggestion.  # noqa: E501
        :rtype: str
        """
        return self._text_unit__document__name

    @text_unit__document__name.setter
    def text_unit__document__name(self, text_unit__document__name):
        """Sets the text_unit__document__name of this TextUnitClassifierSuggestion.


        :param text_unit__document__name: The text_unit__document__name of this TextUnitClassifierSuggestion.  # noqa: E501
        :type text_unit__document__name: str
        """

        self._text_unit__document__name = text_unit__document__name

    @property
    def text_unit__document__document_type(self):
        """Gets the text_unit__document__document_type of this TextUnitClassifierSuggestion.  # noqa: E501


        :return: The text_unit__document__document_type of this TextUnitClassifierSuggestion.  # noqa: E501
        :rtype: str
        """
        return self._text_unit__document__document_type

    @text_unit__document__document_type.setter
    def text_unit__document__document_type(self, text_unit__document__document_type):
        """Sets the text_unit__document__document_type of this TextUnitClassifierSuggestion.


        :param text_unit__document__document_type: The text_unit__document__document_type of this TextUnitClassifierSuggestion.  # noqa: E501
        :type text_unit__document__document_type: str
        """

        self._text_unit__document__document_type = text_unit__document__document_type

    @property
    def text_unit__document__description(self):
        """Gets the text_unit__document__description of this TextUnitClassifierSuggestion.  # noqa: E501


        :return: The text_unit__document__description of this TextUnitClassifierSuggestion.  # noqa: E501
        :rtype: str
        """
        return self._text_unit__document__description

    @text_unit__document__description.setter
    def text_unit__document__description(self, text_unit__document__description):
        """Sets the text_unit__document__description of this TextUnitClassifierSuggestion.


        :param text_unit__document__description: The text_unit__document__description of this TextUnitClassifierSuggestion.  # noqa: E501
        :type text_unit__document__description: str
        """

        self._text_unit__document__description = text_unit__document__description

    @property
    def text_unit__pk(self):
        """Gets the text_unit__pk of this TextUnitClassifierSuggestion.  # noqa: E501


        :return: The text_unit__pk of this TextUnitClassifierSuggestion.  # noqa: E501
        :rtype: str
        """
        return self._text_unit__pk

    @text_unit__pk.setter
    def text_unit__pk(self, text_unit__pk):
        """Sets the text_unit__pk of this TextUnitClassifierSuggestion.


        :param text_unit__pk: The text_unit__pk of this TextUnitClassifierSuggestion.  # noqa: E501
        :type text_unit__pk: str
        """

        self._text_unit__pk = text_unit__pk

    @property
    def class_name(self):
        """Gets the class_name of this TextUnitClassifierSuggestion.  # noqa: E501


        :return: The class_name of this TextUnitClassifierSuggestion.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this TextUnitClassifierSuggestion.


        :param class_name: The class_name of this TextUnitClassifierSuggestion.  # noqa: E501
        :type class_name: str
        """
        if self.local_vars_configuration.client_side_validation and class_name is None:  # noqa: E501
            raise ValueError("Invalid value for `class_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                class_name is not None and len(class_name) > 1024):
            raise ValueError("Invalid value for `class_name`, length must be less than or equal to `1024`")  # noqa: E501

        self._class_name = class_name

    @property
    def class_value(self):
        """Gets the class_value of this TextUnitClassifierSuggestion.  # noqa: E501


        :return: The class_value of this TextUnitClassifierSuggestion.  # noqa: E501
        :rtype: str
        """
        return self._class_value

    @class_value.setter
    def class_value(self, class_value):
        """Sets the class_value of this TextUnitClassifierSuggestion.


        :param class_value: The class_value of this TextUnitClassifierSuggestion.  # noqa: E501
        :type class_value: str
        """
        if self.local_vars_configuration.client_side_validation and class_value is None:  # noqa: E501
            raise ValueError("Invalid value for `class_value`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                class_value is not None and len(class_value) > 1024):
            raise ValueError("Invalid value for `class_value`, length must be less than or equal to `1024`")  # noqa: E501

        self._class_value = class_value

    @property
    def classifier_run(self):
        """Gets the classifier_run of this TextUnitClassifierSuggestion.  # noqa: E501


        :return: The classifier_run of this TextUnitClassifierSuggestion.  # noqa: E501
        :rtype: datetime
        """
        return self._classifier_run

    @classifier_run.setter
    def classifier_run(self, classifier_run):
        """Sets the classifier_run of this TextUnitClassifierSuggestion.


        :param classifier_run: The classifier_run of this TextUnitClassifierSuggestion.  # noqa: E501
        :type classifier_run: datetime
        """

        self._classifier_run = classifier_run

    @property
    def classifier_confidence(self):
        """Gets the classifier_confidence of this TextUnitClassifierSuggestion.  # noqa: E501


        :return: The classifier_confidence of this TextUnitClassifierSuggestion.  # noqa: E501
        :rtype: float
        """
        return self._classifier_confidence

    @classifier_confidence.setter
    def classifier_confidence(self, classifier_confidence):
        """Sets the classifier_confidence of this TextUnitClassifierSuggestion.


        :param classifier_confidence: The classifier_confidence of this TextUnitClassifierSuggestion.  # noqa: E501
        :type classifier_confidence: float
        """

        self._classifier_confidence = classifier_confidence

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
        if not isinstance(other, TextUnitClassifierSuggestion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TextUnitClassifierSuggestion):
            return True

        return self.to_dict() != other.to_dict()