# coding: utf-8

"""
    Asterisk ARI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ari_sync_sdk.models.config_tuple import ConfigTuple

class TestConfigTuple(unittest.TestCase):
    """ConfigTuple unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigTuple:
        """Test ConfigTuple
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigTuple`
        """
        model = ConfigTuple()
        if include_optional:
            return ConfigTuple(
                attribute = '',
                value = ''
            )
        else:
            return ConfigTuple(
                attribute = '',
                value = '',
        )
        """

    def testConfigTuple(self):
        """Test ConfigTuple"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
