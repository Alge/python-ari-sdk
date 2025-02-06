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

from ari_async_sdk.models.bridge_attended_transfer import BridgeAttendedTransfer  # noqa: E501

class TestBridgeAttendedTransfer(unittest.TestCase):
    """BridgeAttendedTransfer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BridgeAttendedTransfer:
        """Test BridgeAttendedTransfer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BridgeAttendedTransfer`
        """
        model = BridgeAttendedTransfer()  # noqa: E501
        if include_optional:
            return BridgeAttendedTransfer(
                destination_application = '',
                destination_bridge = '',
                destination_link_first_leg = ari_async_sdk.models.channel.Channel(
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
                destination_link_second_leg = ari_async_sdk.models.channel.Channel(
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
                destination_threeway_bridge = ari_async_sdk.models.bridge.Bridge(
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
                destination_threeway_channel = ari_async_sdk.models.channel.Channel(
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
                destination_type = '',
                is_external = True,
                replace_channel = ari_async_sdk.models.channel.Channel(
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
                result = '',
                transfer_target = ari_async_sdk.models.channel.Channel(
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
                transferee = ari_async_sdk.models.channel.Channel(
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
                transferer_first_leg = ari_async_sdk.models.channel.Channel(
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
                transferer_first_leg_bridge = ari_async_sdk.models.bridge.Bridge(
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
                transferer_second_leg = ari_async_sdk.models.channel.Channel(
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
                transferer_second_leg_bridge = ari_async_sdk.models.bridge.Bridge(
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
                    video_source_id = '', )
            )
        else:
            return BridgeAttendedTransfer(
                destination_type = '',
                is_external = True,
                result = '',
                transferer_first_leg = ari_async_sdk.models.channel.Channel(
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
                transferer_second_leg = ari_async_sdk.models.channel.Channel(
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

    def testBridgeAttendedTransfer(self):
        """Test BridgeAttendedTransfer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
