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


class ClusterProjectRequest(object):
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
        'n_clusters': 'int',
        'force': 'bool',
        'cluster_by': 'str',
        'method': 'str',
        'require_confirmation': 'bool'
    }

    attribute_map = {
        'n_clusters': 'n_clusters',
        'force': 'force',
        'cluster_by': 'cluster_by',
        'method': 'method',
        'require_confirmation': 'require_confirmation'
    }

    def __init__(self, n_clusters=None, force=None, cluster_by=None, method=None, require_confirmation=None, local_vars_configuration=None):  # noqa: E501
        """ClusterProjectRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._n_clusters = None
        self._force = None
        self._cluster_by = None
        self._method = None
        self._require_confirmation = None
        self.discriminator = None

        self.n_clusters = n_clusters
        if force is not None:
            self.force = force
        self.cluster_by = cluster_by
        self.method = method
        if require_confirmation is not None:
            self.require_confirmation = require_confirmation

    @property
    def n_clusters(self):
        """Gets the n_clusters of this ClusterProjectRequest.  # noqa: E501


        :return: The n_clusters of this ClusterProjectRequest.  # noqa: E501
        :rtype: int
        """
        return self._n_clusters

    @n_clusters.setter
    def n_clusters(self, n_clusters):
        """Sets the n_clusters of this ClusterProjectRequest.


        :param n_clusters: The n_clusters of this ClusterProjectRequest.  # noqa: E501
        :type n_clusters: int
        """
        if self.local_vars_configuration.client_side_validation and n_clusters is None:  # noqa: E501
            raise ValueError("Invalid value for `n_clusters`, must not be `None`")  # noqa: E501

        self._n_clusters = n_clusters

    @property
    def force(self):
        """Gets the force of this ClusterProjectRequest.  # noqa: E501


        :return: The force of this ClusterProjectRequest.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this ClusterProjectRequest.


        :param force: The force of this ClusterProjectRequest.  # noqa: E501
        :type force: bool
        """

        self._force = force

    @property
    def cluster_by(self):
        """Gets the cluster_by of this ClusterProjectRequest.  # noqa: E501


        :return: The cluster_by of this ClusterProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._cluster_by

    @cluster_by.setter
    def cluster_by(self, cluster_by):
        """Sets the cluster_by of this ClusterProjectRequest.


        :param cluster_by: The cluster_by of this ClusterProjectRequest.  # noqa: E501
        :type cluster_by: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_by is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_by`, must not be `None`")  # noqa: E501
        allowed_values = ["term", "date", "text", "definition", "duration", "party", "geoentity", "currency_name", "currency_value"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cluster_by not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cluster_by` ({0}), must be one of {1}"  # noqa: E501
                .format(cluster_by, allowed_values)
            )

        self._cluster_by = cluster_by

    @property
    def method(self):
        """Gets the method of this ClusterProjectRequest.  # noqa: E501


        :return: The method of this ClusterProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ClusterProjectRequest.


        :param method: The method of this ClusterProjectRequest.  # noqa: E501
        :type method: str
        """
        if self.local_vars_configuration.client_side_validation and method is None:  # noqa: E501
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501
        allowed_values = ["kmeans", "minibatchkmeans", "birch"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def require_confirmation(self):
        """Gets the require_confirmation of this ClusterProjectRequest.  # noqa: E501


        :return: The require_confirmation of this ClusterProjectRequest.  # noqa: E501
        :rtype: bool
        """
        return self._require_confirmation

    @require_confirmation.setter
    def require_confirmation(self, require_confirmation):
        """Sets the require_confirmation of this ClusterProjectRequest.


        :param require_confirmation: The require_confirmation of this ClusterProjectRequest.  # noqa: E501
        :type require_confirmation: bool
        """

        self._require_confirmation = require_confirmation

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
        if not isinstance(other, ClusterProjectRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterProjectRequest):
            return True

        return self.to_dict() != other.to_dict()