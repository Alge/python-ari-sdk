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

from ari_async_sdk.models.stasis_end import StasisEnd  # noqa: E501

class TestStasisEnd(unittest.TestCase):
    """StasisEnd unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StasisEnd:
        """Test StasisEnd
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StasisEnd`
        """
        model = StasisEnd()  # noqa: E501
        if include_optional:
            return StasisEnd(
                channel = ari_async_sdk.models.channel.Channel(
                    accountcode = '', 
                    caller = ari_async_sdk.models.caller_id.CallerID(
                        name = '', 
                        number = '', ), 
                    channelvars = ari_async_sdk.models.channelvars.channelvars(), 
                    connected = ari_async_sdk.models.caller_id.CallerID(
                        name = '', 
                        number = '', ), 
                    creationtime = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    dialplan = ari_async_sdk.models.dialplan_cep.DialplanCEP(
                        app_data = '', 
                        app_name = '', 
                        context = '', 
                        exten = '', 
                        priority = 56, ), 
                    id = '', 
                    language = '', 
                    name = '', 
                    state = '', )
            )
        else:
            return StasisEnd(
                channel = ari_async_sdk.models.channel.Channel(
                    accountcode = '', 
                    caller = ari_async_sdk.models.caller_id.CallerID(
                        name = '', 
                        number = '', ), 
                    channelvars = ari_async_sdk.models.channelvars.channelvars(), 
                    connected = ari_async_sdk.models.caller_id.CallerID(
                        name = '', 
                        number = '', ), 
                    creationtime = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    dialplan = ari_async_sdk.models.dialplan_cep.DialplanCEP(
                        app_data = '', 
                        app_name = '', 
                        context = '', 
                        exten = '', 
                        priority = 56, ), 
                    id = '', 
                    language = '', 
                    name = '', 
                    state = '', ),
        )
        """

    def testStasisEnd(self):
        """Test StasisEnd"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
