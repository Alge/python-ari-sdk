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

from ari_sync_sdk.models.mailbox import Mailbox  # noqa: E501

class TestMailbox(unittest.TestCase):
    """Mailbox unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Mailbox:
        """Test Mailbox
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Mailbox`
        """
        model = Mailbox()  # noqa: E501
        if include_optional:
            return Mailbox(
                name = '',
                new_messages = 56,
                old_messages = 56
            )
        else:
            return Mailbox(
                name = '',
                new_messages = 56,
                old_messages = 56,
        )
        """

    def testMailbox(self):
        """Test Mailbox"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
