# coding: utf-8

"""
    Asterisk ARI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ari_sync_sdk.models.status_info import StatusInfo

class TestStatusInfo(unittest.TestCase):
    """StatusInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StatusInfo:
        """Test StatusInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StatusInfo`
        """
        model = StatusInfo()
        if include_optional:
            return StatusInfo(
                last_reload_time = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                startup_time = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else:
            return StatusInfo(
                last_reload_time = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                startup_time = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )
        """

    def testStatusInfo(self):
        """Test StatusInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
