# coding: utf-8

import pytest
import json
from aiohttp import web

from ari_async_sdk.models.application import Application


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_filter(client):
    """Test case for filter

    Filter application events types.
    """
    filter = None
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/ari/applications/{application_name}/eventFilter'.format(application_name='application_name_example'),
        headers=headers,
        json=filter,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get(client):
    """Test case for get

    Get details of an application.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/applications/{application_name}'.format(application_name='application_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list(client):
    """Test case for list

    List all applications.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/applications',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscribe(client):
    """Test case for subscribe

    Subscribe an application to a event source.
    """
    params = [('eventSource', ['event_source_example'])]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/ari/applications/{application_name}/subscription'.format(application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unsubscribe(client):
    """Test case for unsubscribe

    Unsubscribe an application from an event source.
    """
    params = [('eventSource', ['event_source_example'])]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/ari/applications/{application_name}/subscription'.format(application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

