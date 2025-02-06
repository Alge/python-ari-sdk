# coding: utf-8

import pytest
import json
from aiohttp import web

from ari_async_sdk.models.live_recording import LiveRecording
from ari_async_sdk.models.stored_recording import StoredRecording


pytestmark = pytest.mark.asyncio

async def test_cancel(client):
    """Test case for cancel

    Stop a live recording and discard it.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/recordings/live/{recording_name}'.format(recording_name='recording_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_copy_stored(client):
    """Test case for copy_stored

    Copy a stored recording.
    """
    params = [('destinationRecordingName', 'destination_recording_name_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/ari/recordings/stored/{recording_name}/copy'.format(recording_name='recording_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_stored(client):
    """Test case for delete_stored

    Delete a stored recording.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/recordings/stored/{recording_name}'.format(recording_name='recording_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_live(client):
    """Test case for get_live

    List live recordings.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/recordings/live/{recording_name}'.format(recording_name='recording_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stored(client):
    """Test case for get_stored

    Get a stored recording's details.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/recordings/stored/{recording_name}'.format(recording_name='recording_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stored_file(client):
    """Test case for get_stored_file

    Get the file associated with the stored recording.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/recordings/stored/{recording_name}/file'.format(recording_name='recording_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_stored(client):
    """Test case for list_stored

    List recordings that are complete.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/recordings/stored',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_muterecording(client):
    """Test case for muterecording

    Mute a live recording.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/recordings/live/{recording_name}/mute'.format(recording_name='recording_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pause(client):
    """Test case for pause

    Pause a live recording.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/recordings/live/{recording_name}/pause'.format(recording_name='recording_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stoprecording(client):
    """Test case for stoprecording

    Stop a live recording and store it.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/recordings/live/{recording_name}/stop'.format(recording_name='recording_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unmuterecording(client):
    """Test case for unmuterecording

    Unmute a live recording.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/recordings/live/{recording_name}/mute'.format(recording_name='recording_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unpause(client):
    """Test case for unpause

    Unpause a live recording.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/recordings/live/{recording_name}/pause'.format(recording_name='recording_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

