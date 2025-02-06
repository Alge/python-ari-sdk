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

from ari_async_sdk.models.application import Application  # noqa: E501

class TestApplication(unittest.TestCase):
    """Application unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Application:
        """Test Application
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Application`
        """
        model = Application()  # noqa: E501
        if include_optional:
            return Application(
                bridge_ids = [
                    ''
                    ],
                channel_ids = [
                    ''
                    ],
                device_names = [
                    ''
                    ],
                endpoint_ids = [
                    ''
                    ],
                events_allowed = [
                    None
                    ],
                events_disallowed = [
                    None
                    ],
                name = ''
            )
        else:
            return Application(
                bridge_ids = [
                    ''
                    ],
                channel_ids = [
                    ''
                    ],
                device_names = [
                    ''
                    ],
                endpoint_ids = [
                    ''
                    ],
                events_allowed = [
                    None
                    ],
                events_disallowed = [
                    None
                    ],
                name = '',
        )
        """

    def testApplication(self):
        """Test Application"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
