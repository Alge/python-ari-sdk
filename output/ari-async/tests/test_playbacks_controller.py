# coding: utf-8

import pytest
import json
from aiohttp import web

from ari_async_sdk.models.playback import Playback


pytestmark = pytest.mark.asyncio

async def test_control(client):
    """Test case for control

    Control a playback.
    """
    params = [('operation', 'operation_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/playbacks/{playback_id}/control'.format(playback_id='playback_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getplayback(client):
    """Test case for getplayback

    Get a playback's details.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/playbacks/{playback_id}'.format(playback_id='playback_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop(client):
    """Test case for stop

    Stop a playback.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/playbacks/{playback_id}'.format(playback_id='playback_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

