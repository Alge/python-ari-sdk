# coding: utf-8

"""
    Asterisk ARI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ari_sync_sdk.api.bridges_api import BridgesApi


class TestBridgesApi(unittest.TestCase):
    """BridgesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BridgesApi()

    def tearDown(self) -> None:
        pass

    def test_add_channel(self) -> None:
        """Test case for add_channel

        Add a channel to a bridge.
        """
        pass

    def test_clear_video_source(self) -> None:
        """Test case for clear_video_source

        Removes any explicit video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants. When no explicit video source is set, talk detection will be used to determine the active video stream.
        """
        pass

    def test_create(self) -> None:
        """Test case for create

        Create a new bridge.
        """
        pass

    def test_create_with_id(self) -> None:
        """Test case for create_with_id

        Create a new bridge or updates an existing one.
        """
        pass

    def test_destroy(self) -> None:
        """Test case for destroy

        Shut down a bridge.
        """
        pass

    def test_getbridge(self) -> None:
        """Test case for getbridge

        Get bridge details.
        """
        pass

    def test_listbridges(self) -> None:
        """Test case for listbridges

        List all active bridges in Asterisk.
        """
        pass

    def test_play(self) -> None:
        """Test case for play

        Start playback of media on a bridge.
        """
        pass

    def test_play_with_id(self) -> None:
        """Test case for play_with_id

        Start playback of media on a bridge.
        """
        pass

    def test_record(self) -> None:
        """Test case for record

        Start a recording.
        """
        pass

    def test_remove_channel(self) -> None:
        """Test case for remove_channel

        Remove a channel from a bridge.
        """
        pass

    def test_set_video_source(self) -> None:
        """Test case for set_video_source

        Set a channel as the video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants.
        """
        pass

    def test_start_moh(self) -> None:
        """Test case for start_moh

        Play music on hold to a bridge or change the MOH class that is playing.
        """
        pass

    def test_stop_moh(self) -> None:
        """Test case for stop_moh

        Stop playing music on hold to a bridge.
        """
        pass


if __name__ == '__main__':
    unittest.main()
