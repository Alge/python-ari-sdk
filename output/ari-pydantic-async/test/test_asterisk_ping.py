# coding: utf-8

"""
    Asterisk ARI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from ari_async_sdk.models.asterisk_ping import AsteriskPing  # noqa: E501

class TestAsteriskPing(unittest.TestCase):
    """AsteriskPing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AsteriskPing:
        """Test AsteriskPing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AsteriskPing`
        """
        model = AsteriskPing()  # noqa: E501
        if include_optional:
            return AsteriskPing(
                asterisk_id = '',
                ping = '',
                timestamp = ''
            )
        else:
            return AsteriskPing(
                asterisk_id = '',
                ping = '',
                timestamp = '',
        )
        """

    def testAsteriskPing(self):
        """Test AsteriskPing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
