# coding: utf-8

import pytest
import json
from aiohttp import web

from ari_async_sdk.models.channel import Channel
from ari_async_sdk.models.live_recording import LiveRecording
from ari_async_sdk.models.playback import Playback
from ari_async_sdk.models.rt_pstat import RTPstat
from ari_async_sdk.models.variable import Variable


pytestmark = pytest.mark.asyncio

async def test_add_moh(client):
    """Test case for add_moh

    Play music on hold to a channel.
    """
    params = [('mohClass', 'moh_class_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/moh'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_answer(client):
    """Test case for answer

    Answer a channel.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/answer'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_continue_in_dialplan(client):
    """Test case for continue_in_dialplan

    Exit application; continue execution in the dialplan.
    """
    params = [('context', 'context_example'),
                    ('extension', 'extension_example'),
                    ('priority', 56),
                    ('label', 'label_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/continue'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_createchannel(client):
    """Test case for createchannel

    Create channel.
    """
    variables = None
    params = [('endpoint', 'endpoint_example'),
                    ('app', 'app_example'),
                    ('appArgs', 'app_args_example'),
                    ('channelId', 'channel_id_example'),
                    ('otherChannelId', 'other_channel_id_example'),
                    ('originator', 'originator_example'),
                    ('formats', 'formats_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/create',
        headers=headers,
        json=variables,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deletemoh(client):
    """Test case for deletemoh

    Stop playing music on hold to a channel.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/channels/{channel_id}/moh'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dial(client):
    """Test case for dial

    Dial a created channel.
    """
    params = [('caller', 'caller_example'),
                    ('timeout', 0)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/dial'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_external_media(client):
    """Test case for external_media

    Start an External Media session.
    """
    variables = None
    params = [('channelId', 'channel_id_example'),
                    ('app', 'app_example'),
                    ('external_host', 'external_host_example'),
                    ('encapsulation', 'rtp'),
                    ('transport', 'udp'),
                    ('connection_type', 'client'),
                    ('format', 'format_example'),
                    ('direction', 'both'),
                    ('data', 'data_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/externalMedia',
        headers=headers,
        json=variables,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_var(client):
    """Test case for get_channel_var

    Get the value of a channel variable or function.
    """
    params = [('variable', 'variable_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/channels/{channel_id}/variable'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getchannel(client):
    """Test case for getchannel

    Channel details.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/channels/{channel_id}'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hangup(client):
    """Test case for hangup

    Delete (i.e. hangup) a channel.
    """
    params = [('reason_code', 'reason_code_example'),
                    ('reason', 'reason_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/channels/{channel_id}'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hold(client):
    """Test case for hold

    Hold a channel.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/hold'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listchannels(client):
    """Test case for listchannels

    List all active channels in Asterisk.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/channels',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move(client):
    """Test case for move

    Move the channel from one Stasis application to another.
    """
    params = [('app', 'app_example'),
                    ('appArgs', 'app_args_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/move'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mute(client):
    """Test case for mute

    Mute a channel.
    """
    params = [('direction', 'both')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/mute'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_originate(client):
    """Test case for originate

    Create a new channel (originate).
    """
    variables = None
    params = [('endpoint', 'endpoint_example'),
                    ('extension', 'extension_example'),
                    ('context', 'context_example'),
                    ('priority', 56),
                    ('label', 'label_example'),
                    ('app', 'app_example'),
                    ('appArgs', 'app_args_example'),
                    ('callerId', 'caller_id_example'),
                    ('timeout', 30),
                    ('channelId', 'channel_id_example'),
                    ('otherChannelId', 'other_channel_id_example'),
                    ('originator', 'originator_example'),
                    ('formats', 'formats_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ari/channels',
        headers=headers,
        json=variables,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_originate_with_id(client):
    """Test case for originate_with_id

    Create a new channel (originate with id).
    """
    variables = None
    params = [('endpoint', 'endpoint_example'),
                    ('extension', 'extension_example'),
                    ('context', 'context_example'),
                    ('priority', 56),
                    ('label', 'label_example'),
                    ('app', 'app_example'),
                    ('appArgs', 'app_args_example'),
                    ('callerId', 'caller_id_example'),
                    ('timeout', 30),
                    ('otherChannelId', 'other_channel_id_example'),
                    ('originator', 'originator_example'),
                    ('formats', 'formats_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}'.format(channel_id='channel_id_example'),
        headers=headers,
        json=variables,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_play_sound_with_id(client):
    """Test case for play_sound_with_id

    Start playback of media and specify the playbackId.
    """
    params = [('media', ['media_example']),
                    ('lang', 'lang_example'),
                    ('offsetms', 56),
                    ('skipms', 3000)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/play/{playback_id}'.format(channel_id='channel_id_example', playback_id='playback_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_playsound(client):
    """Test case for playsound

    Start playback of media.
    """
    params = [('media', ['media_example']),
                    ('lang', 'lang_example'),
                    ('offsetms', 56),
                    ('skipms', 3000),
                    ('playbackId', 'playback_id_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/play'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recordchannel(client):
    """Test case for recordchannel

    Start a recording.
    """
    params = [('name', 'name_example'),
                    ('format', 'format_example'),
                    ('maxDurationSeconds', 0),
                    ('maxSilenceSeconds', 0),
                    ('ifExists', 'fail'),
                    ('beep', False),
                    ('terminateOn', 'none')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/record'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redirect(client):
    """Test case for redirect

    Redirect the channel to a different location.
    """
    params = [('endpoint', 'endpoint_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/redirect'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ring(client):
    """Test case for ring

    Indicate ringing to a channel.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/ring'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ring_stop(client):
    """Test case for ring_stop

    Stop ringing indication on a channel if locally generated.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/channels/{channel_id}/ring'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rtpstatistics(client):
    """Test case for rtpstatistics

    RTP stats on a channel.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/channels/{channel_id}/rtp_statistics'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_dtmf(client):
    """Test case for send_dtmf

    Send provided DTMF to a given channel.
    """
    params = [('dtmf', 'dtmf_example'),
                    ('before', 0),
                    ('between', 100),
                    ('duration', 100),
                    ('after', 0)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/dtmf'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_channel_var(client):
    """Test case for set_channel_var

    Set the value of a channel variable or function.
    """
    params = [('variable', 'variable_example'),
                    ('value', 'value_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/variable'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snoop_channel(client):
    """Test case for snoop_channel

    Start snooping.
    """
    params = [('spy', 'none'),
                    ('whisper', 'none'),
                    ('app', 'app_example'),
                    ('appArgs', 'app_args_example'),
                    ('snoopId', 'snoop_id_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/snoop'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snoop_channel_with_id(client):
    """Test case for snoop_channel_with_id

    Start snooping.
    """
    params = [('spy', 'none'),
                    ('whisper', 'none'),
                    ('app', 'app_example'),
                    ('appArgs', 'app_args_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/snoop/{snoop_id}'.format(channel_id='channel_id_example', snoop_id='snoop_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_silence(client):
    """Test case for start_silence

    Play silence to a channel.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/channels/{channel_id}/silence'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_silence(client):
    """Test case for stop_silence

    Stop playing silence to a channel.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/channels/{channel_id}/silence'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unhold(client):
    """Test case for unhold

    Remove a channel from hold.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/channels/{channel_id}/hold'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unmute(client):
    """Test case for unmute

    Unmute a channel.
    """
    params = [('direction', 'both')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/channels/{channel_id}/mute'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

