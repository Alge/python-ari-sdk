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

from ari_async_sdk.models.channel_userevent import ChannelUserevent  # noqa: E501

class TestChannelUserevent(unittest.TestCase):
    """ChannelUserevent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChannelUserevent:
        """Test ChannelUserevent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChannelUserevent`
        """
        model = ChannelUserevent()  # noqa: E501
        if include_optional:
            return ChannelUserevent(
                bridge = ari_async_sdk.models.bridge.Bridge(
                    bridge_class = '', 
                    bridge_type = '', 
                    channels = [
                        ''
                        ], 
                    creationtime = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    creator = '', 
                    id = '', 
                    name = '', 
                    technology = '', 
                    video_mode = '', 
                    video_source_id = '', ),
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
                endpoint = ari_async_sdk.models.endpoint.Endpoint(
                    channel_ids = [
                        ''
                        ], 
                    resource = '', 
                    state = '', 
                    technology = '', ),
                eventname = '',
                userevent = None
            )
        else:
            return ChannelUserevent(
                eventname = '',
                userevent = None,
        )
        """

    def testChannelUserevent(self):
        """Test ChannelUserevent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
