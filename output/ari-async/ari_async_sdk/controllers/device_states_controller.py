from typing import List, Dict
from aiohttp import web

from ari_async_sdk.models.device_state import DeviceState
from ari_async_sdk import util


async def delete(request: web.Request, device_name) -> web.Response:
    """Destroy a device-state controlled by ARI.

    

    :param device_name: Name of the device
    :type device_name: str

    """
    return web.Response(status=200)


async def getdevicestate(request: web.Request, device_name) -> web.Response:
    """Retrieve the current state of a device.

    

    :param device_name: Name of the device
    :type device_name: str

    """
    return web.Response(status=200)


async def list_device_states(request: web.Request, ) -> web.Response:
    """List all ARI controlled device states.

    


    """
    return web.Response(status=200)


async def update(request: web.Request, device_name, device_state) -> web.Response:
    """Change the state of a device controlled by ARI. (Note - implicitly creates the device state).

    

    :param device_name: Name of the device
    :type device_name: str
    :param device_state: Device state value
    :type device_state: str

    """
    return web.Response(status=200)
