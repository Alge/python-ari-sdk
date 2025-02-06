# coding: utf-8

import pytest
import json
from aiohttp import web

from ari_async_sdk.models.device_state import DeviceState


pytestmark = pytest.mark.asyncio

async def test_delete(client):
    """Test case for delete

    Destroy a device-state controlled by ARI.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/deviceStates/{device_name}'.format(device_name='device_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getdevicestate(client):
    """Test case for getdevicestate

    Retrieve the current state of a device.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/deviceStates/{device_name}'.format(device_name='device_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_device_states(client):
    """Test case for list_device_states

    List all ARI controlled device states.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/deviceStates',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update(client):
    """Test case for update

    Change the state of a device controlled by ARI. (Note - implicitly creates the device state).
    """
    params = [('deviceState', 'device_state_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/ari/deviceStates/{device_name}'.format(device_name='device_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

