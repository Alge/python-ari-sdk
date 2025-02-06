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

from ari_async_sdk.models.asterisk_info import AsteriskInfo  # noqa: E501

class TestAsteriskInfo(unittest.TestCase):
    """AsteriskInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AsteriskInfo:
        """Test AsteriskInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AsteriskInfo`
        """
        model = AsteriskInfo()  # noqa: E501
        if include_optional:
            return AsteriskInfo(
                build = ari_async_sdk.models.build_info.BuildInfo(
                    date = '', 
                    kernel = '', 
                    machine = '', 
                    options = '', 
                    os = '', 
                    user = '', ),
                config = ari_async_sdk.models.config_info.ConfigInfo(
                    default_language = '', 
                    max_channels = 56, 
                    max_load = 1.337, 
                    max_open_files = 56, 
                    name = '', 
                    setid = ari_async_sdk.models.set_id.SetId(
                        group = '', 
                        user = '', ), ),
                status = ari_async_sdk.models.status_info.StatusInfo(
                    last_reload_time = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    startup_time = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), ),
                system = ari_async_sdk.models.system_info.SystemInfo(
                    entity_id = '', 
                    version = '', )
            )
        else:
            return AsteriskInfo(
        )
        """

    def testAsteriskInfo(self):
        """Test AsteriskInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
