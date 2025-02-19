# coding: utf-8

"""
    Asterisk ARI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ari_sync_sdk.api.channels_api import ChannelsApi  # noqa: E501


class TestChannelsApi(unittest.TestCase):
    """ChannelsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ChannelsApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_add_moh(self) -> None:
        """Test case for add_moh

        Play music on hold to a channel.  # noqa: E501
        """
        pass

    def test_answer(self) -> None:
        """Test case for answer

        Answer a channel.  # noqa: E501
        """
        pass

    def test_continue_in_dialplan(self) -> None:
        """Test case for continue_in_dialplan

        Exit application; continue execution in the dialplan.  # noqa: E501
        """
        pass

    def test_createchannel(self) -> None:
        """Test case for createchannel

        Create channel.  # noqa: E501
        """
        pass

    def test_deletemoh(self) -> None:
        """Test case for deletemoh

        Stop playing music on hold to a channel.  # noqa: E501
        """
        pass

    def test_dial(self) -> None:
        """Test case for dial

        Dial a created channel.  # noqa: E501
        """
        pass

    def test_external_media(self) -> None:
        """Test case for external_media

        Start an External Media session.  # noqa: E501
        """
        pass

    def test_get_channel_var(self) -> None:
        """Test case for get_channel_var

        Get the value of a channel variable or function.  # noqa: E501
        """
        pass

    def test_getchannel(self) -> None:
        """Test case for getchannel

        Channel details.  # noqa: E501
        """
        pass

    def test_hangup(self) -> None:
        """Test case for hangup

        Delete (i.e. hangup) a channel.  # noqa: E501
        """
        pass

    def test_hold(self) -> None:
        """Test case for hold

        Hold a channel.  # noqa: E501
        """
        pass

    def test_listchannels(self) -> None:
        """Test case for listchannels

        List all active channels in Asterisk.  # noqa: E501
        """
        pass

    def test_move(self) -> None:
        """Test case for move

        Move the channel from one Stasis application to another.  # noqa: E501
        """
        pass

    def test_mute(self) -> None:
        """Test case for mute

        Mute a channel.  # noqa: E501
        """
        pass

    def test_originate(self) -> None:
        """Test case for originate

        Create a new channel (originate).  # noqa: E501
        """
        pass

    def test_originate_with_id(self) -> None:
        """Test case for originate_with_id

        Create a new channel (originate with id).  # noqa: E501
        """
        pass

    def test_play_sound_with_id(self) -> None:
        """Test case for play_sound_with_id

        Start playback of media and specify the playbackId.  # noqa: E501
        """
        pass

    def test_playsound(self) -> None:
        """Test case for playsound

        Start playback of media.  # noqa: E501
        """
        pass

    def test_recordchannel(self) -> None:
        """Test case for recordchannel

        Start a recording.  # noqa: E501
        """
        pass

    def test_redirect(self) -> None:
        """Test case for redirect

        Redirect the channel to a different location.  # noqa: E501
        """
        pass

    def test_ring(self) -> None:
        """Test case for ring

        Indicate ringing to a channel.  # noqa: E501
        """
        pass

    def test_ring_stop(self) -> None:
        """Test case for ring_stop

        Stop ringing indication on a channel if locally generated.  # noqa: E501
        """
        pass

    def test_rtpstatistics(self) -> None:
        """Test case for rtpstatistics

        RTP stats on a channel.  # noqa: E501
        """
        pass

    def test_send_dtmf(self) -> None:
        """Test case for send_dtmf

        Send provided DTMF to a given channel.  # noqa: E501
        """
        pass

    def test_set_channel_var(self) -> None:
        """Test case for set_channel_var

        Set the value of a channel variable or function.  # noqa: E501
        """
        pass

    def test_snoop_channel(self) -> None:
        """Test case for snoop_channel

        Start snooping.  # noqa: E501
        """
        pass

    def test_snoop_channel_with_id(self) -> None:
        """Test case for snoop_channel_with_id

        Start snooping.  # noqa: E501
        """
        pass

    def test_start_silence(self) -> None:
        """Test case for start_silence

        Play silence to a channel.  # noqa: E501
        """
        pass

    def test_stop_silence(self) -> None:
        """Test case for stop_silence

        Stop playing silence to a channel.  # noqa: E501
        """
        pass

    def test_unhold(self) -> None:
        """Test case for unhold

        Remove a channel from hold.  # noqa: E501
        """
        pass

    def test_unmute(self) -> None:
        """Test case for unmute

        Unmute a channel.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
