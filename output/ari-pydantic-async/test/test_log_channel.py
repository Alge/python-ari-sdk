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

from ari_async_sdk.models.log_channel import LogChannel  # noqa: E501

class TestLogChannel(unittest.TestCase):
    """LogChannel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LogChannel:
        """Test LogChannel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LogChannel`
        """
        model = LogChannel()  # noqa: E501
        if include_optional:
            return LogChannel(
                channel = '',
                configuration = '',
                status = '',
                type = ''
            )
        else:
            return LogChannel(
                channel = '',
                configuration = '',
                status = '',
                type = '',
        )
        """

    def testLogChannel(self):
        """Test LogChannel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
