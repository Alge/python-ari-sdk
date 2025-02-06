from typing import List, Dict
from aiohttp import web

from ari_async_sdk.models.asterisk_info import AsteriskInfo
from ari_async_sdk.models.asterisk_ping import AsteriskPing
from ari_async_sdk.models.config_tuple import ConfigTuple
from ari_async_sdk.models.log_channel import LogChannel
from ari_async_sdk.models.module import Module
from ari_async_sdk.models.variable import Variable
from ari_async_sdk import util


async def add_log(request: web.Request, log_channel_name, configuration) -> web.Response:
    """Adds a log channel.

    

    :param log_channel_name: The log channel to add
    :type log_channel_name: str
    :param configuration: levels of the log channel
    :type configuration: str

    """
    return web.Response(status=200)


async def delete_log(request: web.Request, log_channel_name) -> web.Response:
    """Deletes a log channel.

    

    :param log_channel_name: Log channels name
    :type log_channel_name: str

    """
    return web.Response(status=200)


async def delete_object(request: web.Request, config_class, object_type, id) -> web.Response:
    """Delete a dynamic configuration object.

    

    :param config_class: The configuration class containing dynamic configuration objects.
    :type config_class: str
    :param object_type: The type of configuration object to delete.
    :type object_type: str
    :param id: The unique identifier of the object to delete.
    :type id: str

    """
    return web.Response(status=200)


async def get_global_var(request: web.Request, variable) -> web.Response:
    """Get the value of a global variable.

    

    :param variable: The variable to get
    :type variable: str

    """
    return web.Response(status=200)


async def get_info(request: web.Request, only=None) -> web.Response:
    """Gets Asterisk system information.

    

    :param only: Filter information returned
    :type only: List[str]

    """
    return web.Response(status=200)


async def get_module(request: web.Request, module_name) -> web.Response:
    """Get Asterisk module information.

    

    :param module_name: Module&#39;s name
    :type module_name: str

    """
    return web.Response(status=200)


async def get_object(request: web.Request, config_class, object_type, id) -> web.Response:
    """Retrieve a dynamic configuration object.

    

    :param config_class: The configuration class containing dynamic configuration objects.
    :type config_class: str
    :param object_type: The type of configuration object to retrieve.
    :type object_type: str
    :param id: The unique identifier of the object to retrieve.
    :type id: str

    """
    return web.Response(status=200)


async def list_log_channels(request: web.Request, ) -> web.Response:
    """Gets Asterisk log channel information.

    


    """
    return web.Response(status=200)


async def list_modules(request: web.Request, ) -> web.Response:
    """List Asterisk modules.

    


    """
    return web.Response(status=200)


async def load_module(request: web.Request, module_name) -> web.Response:
    """Load an Asterisk module.

    

    :param module_name: Module&#39;s name
    :type module_name: str

    """
    return web.Response(status=200)


async def ping(request: web.Request, ) -> web.Response:
    """Response pong message.

    


    """
    return web.Response(status=200)


async def reload_module(request: web.Request, module_name) -> web.Response:
    """Reload an Asterisk module.

    

    :param module_name: Module&#39;s name
    :type module_name: str

    """
    return web.Response(status=200)


async def rotate_log(request: web.Request, log_channel_name) -> web.Response:
    """Rotates a log channel.

    

    :param log_channel_name: Log channel&#39;s name
    :type log_channel_name: str

    """
    return web.Response(status=200)


async def set_global_var(request: web.Request, variable, value=None) -> web.Response:
    """Set the value of a global variable.

    

    :param variable: The variable to set
    :type variable: str
    :param value: The value to set the variable to
    :type value: str

    """
    return web.Response(status=200)


async def unload_module(request: web.Request, module_name) -> web.Response:
    """Unload an Asterisk module.

    

    :param module_name: Module&#39;s name
    :type module_name: str

    """
    return web.Response(status=200)


async def update_object(request: web.Request, config_class, object_type, id, fields=None) -> web.Response:
    """Create or update a dynamic configuration object.

    

    :param config_class: The configuration class containing dynamic configuration objects.
    :type config_class: str
    :param object_type: The type of configuration object to create or update.
    :type object_type: str
    :param id: The unique identifier of the object to create or update.
    :type id: str
    :param fields: The body object should have a value that is a list of ConfigTuples, which provide the fields to update. Ex. [ { \&quot;attribute\&quot;: \&quot;directmedia\&quot;, \&quot;value\&quot;: \&quot;false\&quot; } ]
    :type fields: 

    """
    return web.Response(status=200)
