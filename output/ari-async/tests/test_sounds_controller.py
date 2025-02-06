# coding: utf-8

import pytest
import json
from aiohttp import web

from ari_async_sdk.models.sound import Sound


pytestmark = pytest.mark.asyncio

async def test_getsound(client):
    """Test case for getsound

    Get a sound's details.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/sounds/{sound_id}'.format(sound_id='sound_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listsounds(client):
    """Test case for listsounds

    List all sounds.
    """
    params = [('lang', 'lang_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/sounds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

