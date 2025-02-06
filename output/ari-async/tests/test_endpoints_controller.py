# coding: utf-8

import pytest
import json
from aiohttp import web

from ari_async_sdk.models.endpoint import Endpoint


pytestmark = pytest.mark.asyncio

async def test_getendpoint(client):
    """Test case for getendpoint

    Details for an endpoint.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/endpoints/{tech}/{resource}'.format(tech='tech_example', resource='resource_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_by_tech(client):
    """Test case for list_by_tech

    List available endoints for a given endpoint technology.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/endpoints/{tech}'.format(tech='tech_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listendpoints(client):
    """Test case for listendpoints

    List all endpoints.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/endpoints',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_send_message(client):
    """Test case for send_message

    Send a message to some technology URI or endpoint.
    """
    variables = None
    params = [('to', 'to_example'),
                    ('from', '_from_example'),
                    ('body', 'body_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/ari/endpoints/sendMessage',
        headers=headers,
        json=variables,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_send_message_to_endpoint(client):
    """Test case for send_message_to_endpoint

    Send a message to some endpoint in a technology.
    """
    variables = None
    params = [('from', '_from_example'),
                    ('body', 'body_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/ari/endpoints/{tech}/{resource}/sendMessage'.format(tech='tech_example', resource='resource_example'),
        headers=headers,
        json=variables,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

