# coding: utf-8

"""
    Asterisk ARI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ari_sync_sdk.models.contact_info import ContactInfo

class TestContactInfo(unittest.TestCase):
    """ContactInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContactInfo:
        """Test ContactInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContactInfo`
        """
        model = ContactInfo()
        if include_optional:
            return ContactInfo(
                aor = '',
                contact_status = '',
                roundtrip_usec = '',
                uri = ''
            )
        else:
            return ContactInfo(
                aor = '',
                contact_status = '',
                uri = '',
        )
        """

    def testContactInfo(self):
        """Test ContactInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
