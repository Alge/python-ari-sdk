# coding: utf-8

import pytest
import json
from aiohttp import web

from ari_async_sdk.models.bridge import Bridge
from ari_async_sdk.models.live_recording import LiveRecording
from ari_async_sdk.models.playback import Playback


pytestmark = pytest.mark.asyncio

async def test_add_channel(client):
    """Test case for add_channel

    Add a channel to a bridge.
    """
    params = [('channel', ['channel_example']),
                    ('role', 'role_example'),
                    ('absorbDTMF', False),
                    ('mute', False),
                    ('inhibitConnectedLineUpdates', False)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/bridges/{bridge_id}/addChannel'.format(bridge_id='bridge_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clear_video_source(client):
    """Test case for clear_video_source

    Removes any explicit video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants. When no explicit video source is set, talk detection will be used to determine the active video stream.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/bridges/{bridge_id}/videoSource'.format(bridge_id='bridge_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create(client):
    """Test case for create

    Create a new bridge.
    """
    params = [('type', 'type_example'),
                    ('bridgeId', 'bridge_id_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/ari/bridges',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_with_id(client):
    """Test case for create_with_id

    Create a new bridge or updates an existing one.
    """
    params = [('type', 'type_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/ari/bridges/{bridge_id}'.format(bridge_id='bridge_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destroy(client):
    """Test case for destroy

    Shut down a bridge.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/bridges/{bridge_id}'.format(bridge_id='bridge_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getbridge(client):
    """Test case for getbridge

    Get bridge details.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/bridges/{bridge_id}'.format(bridge_id='bridge_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listbridges(client):
    """Test case for listbridges

    List all active bridges in Asterisk.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/bridges',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_play(client):
    """Test case for play

    Start playback of media on a bridge.
    """
    params = [('media', ['media_example']),
                    ('lang', 'lang_example'),
                    ('offsetms', 0),
                    ('skipms', 3000),
                    ('playbackId', 'playback_id_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/ari/bridges/{bridge_id}/play'.format(bridge_id='bridge_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_play_with_id(client):
    """Test case for play_with_id

    Start playback of media on a bridge.
    """
    params = [('media', ['media_example']),
                    ('lang', 'lang_example'),
                    ('offsetms', 0),
                    ('skipms', 3000)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/ari/bridges/{bridge_id}/play/{playback_id}'.format(bridge_id='bridge_id_example', playback_id='playback_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_record(client):
    """Test case for record

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
        path='/ari/bridges/{bridge_id}/record'.format(bridge_id='bridge_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_channel(client):
    """Test case for remove_channel

    Remove a channel from a bridge.
    """
    params = [('channel', ['channel_example'])]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/bridges/{bridge_id}/removeChannel'.format(bridge_id='bridge_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_video_source(client):
    """Test case for set_video_source

    Set a channel as the video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/bridges/{bridge_id}/videoSource/{channel_id}'.format(bridge_id='bridge_id_example', channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_moh(client):
    """Test case for start_moh

    Play music on hold to a bridge or change the MOH class that is playing.
    """
    params = [('mohClass', 'moh_class_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/bridges/{bridge_id}/moh'.format(bridge_id='bridge_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_moh(client):
    """Test case for stop_moh

    Stop playing music on hold to a bridge.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/bridges/{bridge_id}/moh'.format(bridge_id='bridge_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

