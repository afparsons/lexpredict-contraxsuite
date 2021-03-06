# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.project_update import ProjectUpdate  # noqa: E501
from openapi_client.rest import ApiException

class TestProjectUpdate(unittest.TestCase):
    """ProjectUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.project_update.ProjectUpdate()  # noqa: E501
        if include_optional :
            return ProjectUpdate(
                pk = 56, 
                name = '0', 
                description = '0', 
                status = 56, 
                send_email_notification = True, 
                owners = [
                    56
                    ], 
                reviewers = [
                    56
                    ], 
                super_reviewers = [
                    56
                    ], 
                junior_reviewers = [
                    56
                    ], 
                type = '0', 
                hide_clause_review = True
            )
        else :
            return ProjectUpdate(
                name = '0',
        )

    def testProjectUpdate(self):
        """Test ProjectUpdate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
