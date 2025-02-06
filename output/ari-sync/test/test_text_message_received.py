# coding: utf-8

"""
    Asterisk ARI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ari_sync_sdk.models.text_message_received import TextMessageReceived

class TestTextMessageReceived(unittest.TestCase):
    """TextMessageReceived unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextMessageReceived:
        """Test TextMessageReceived
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TextMessageReceived`
        """
        model = TextMessageReceived()
        if include_optional:
            return TextMessageReceived(
                endpoint = ari_sync_sdk.models.endpoint.Endpoint(
                    channel_ids = [
                        ''
                        ], 
                    resource = '', 
                    state = '', 
                    technology = '', ),
                message = ari_sync_sdk.models.text_message.TextMessage(
                    body = '', 
                    from = '', 
                    to = '', 
                    variables = ari_sync_sdk.models.variables.variables(), )
            )
        else:
            return TextMessageReceived(
                message = ari_sync_sdk.models.text_message.TextMessage(
                    body = '', 
                    from = '', 
                    to = '', 
                    variables = ari_sync_sdk.models.variables.variables(), ),
        )
        """

    def testTextMessageReceived(self):
        """Test TextMessageReceived"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
