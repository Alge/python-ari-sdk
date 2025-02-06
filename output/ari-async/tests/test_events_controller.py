# coding: utf-8

import pytest
import json
from aiohttp import web

from ari_async_sdk.models.message import Message


pytestmark = pytest.mark.asyncio

async def test_event_websocket(client):
    """Test case for event_websocket

    WebSocket connection for events.
    """
    params = [('app', ['app_example']),
                    ('subscribeAll', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_user_event(client):
    """Test case for user_event

    Generate a user event.
    """
    variables = None
    params = [('application', 'application_example'),
                    ('source', ['source_example'])]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ari/events/user/{event_name}'.format(event_name='event_name_example'),
        headers=headers,
        json=variables,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

