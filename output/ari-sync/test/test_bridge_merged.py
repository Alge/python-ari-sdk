# coding: utf-8

"""
    Asterisk ARI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ari_sync_sdk.models.bridge_merged import BridgeMerged

class TestBridgeMerged(unittest.TestCase):
    """BridgeMerged unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BridgeMerged:
        """Test BridgeMerged
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BridgeMerged`
        """
        model = BridgeMerged()
        if include_optional:
            return BridgeMerged(
                bridge = ari_sync_sdk.models.bridge.Bridge(
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
                bridge_from = ari_sync_sdk.models.bridge.Bridge(
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
            return BridgeMerged(
                bridge = ari_sync_sdk.models.bridge.Bridge(
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
                bridge_from = ari_sync_sdk.models.bridge.Bridge(
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
        )
        """

    def testBridgeMerged(self):
        """Test BridgeMerged"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
