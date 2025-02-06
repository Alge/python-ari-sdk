# coding: utf-8

import pytest
import json
from aiohttp import web

from ari_async_sdk.models.asterisk_info import AsteriskInfo
from ari_async_sdk.models.asterisk_ping import AsteriskPing
from ari_async_sdk.models.config_tuple import ConfigTuple
from ari_async_sdk.models.log_channel import LogChannel
from ari_async_sdk.models.module import Module
from ari_async_sdk.models.variable import Variable


pytestmark = pytest.mark.asyncio

async def test_add_log(client):
    """Test case for add_log

    Adds a log channel.
    """
    params = [('configuration', 'configuration_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/asterisk/logging/{log_channel_name}'.format(log_channel_name='log_channel_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_log(client):
    """Test case for delete_log

    Deletes a log channel.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/asterisk/logging/{log_channel_name}'.format(log_channel_name='log_channel_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_object(client):
    """Test case for delete_object

    Delete a dynamic configuration object.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/asterisk/config/dynamic/{config_class}/{object_type}/{id}'.format(config_class='config_class_example', object_type='object_type_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_global_var(client):
    """Test case for get_global_var

    Get the value of a global variable.
    """
    params = [('variable', 'variable_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/asterisk/variable',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_info(client):
    """Test case for get_info

    Gets Asterisk system information.
    """
    params = [('only', ['only_example'])]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/asterisk/info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_module(client):
    """Test case for get_module

    Get Asterisk module information.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/asterisk/modules/{module_name}'.format(module_name='module_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_object(client):
    """Test case for get_object

    Retrieve a dynamic configuration object.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/asterisk/config/dynamic/{config_class}/{object_type}/{id}'.format(config_class='config_class_example', object_type='object_type_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_log_channels(client):
    """Test case for list_log_channels

    Gets Asterisk log channel information.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/asterisk/logging',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_modules(client):
    """Test case for list_modules

    List Asterisk modules.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/asterisk/modules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_module(client):
    """Test case for load_module

    Load an Asterisk module.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/asterisk/modules/{module_name}'.format(module_name='module_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ping(client):
    """Test case for ping

    Response pong message.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/asterisk/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reload_module(client):
    """Test case for reload_module

    Reload an Asterisk module.
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/ari/asterisk/modules/{module_name}'.format(module_name='module_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rotate_log(client):
    """Test case for rotate_log

    Rotates a log channel.
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/ari/asterisk/logging/{log_channel_name}/rotate'.format(log_channel_name='log_channel_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_global_var(client):
    """Test case for set_global_var

    Set the value of a global variable.
    """
    params = [('variable', 'variable_example'),
                    ('value', 'value_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/ari/asterisk/variable',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unload_module(client):
    """Test case for unload_module

    Unload an Asterisk module.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/asterisk/modules/{module_name}'.format(module_name='module_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_object(client):
    """Test case for update_object

    Create or update a dynamic configuration object.
    """
    fields = None
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/ari/asterisk/config/dynamic/{config_class}/{object_type}/{id}'.format(config_class='config_class_example', object_type='object_type_example', id='id_example'),
        headers=headers,
        json=fields,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

