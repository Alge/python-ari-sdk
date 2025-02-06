from typing import List, Dict
from aiohttp import web

from ari_async_sdk.models.playback import Playback
from ari_async_sdk import util


async def control(request: web.Request, playback_id, operation) -> web.Response:
    """Control a playback.

    

    :param playback_id: Playback&#39;s id
    :type playback_id: str
    :param operation: Operation to perform on the playback.
    :type operation: str

    """
    return web.Response(status=200)


async def getplayback(request: web.Request, playback_id) -> web.Response:
    """Get a playback&#39;s details.

    

    :param playback_id: Playback&#39;s id
    :type playback_id: str

    """
    return web.Response(status=200)


async def stop(request: web.Request, playback_id) -> web.Response:
    """Stop a playback.

    

    :param playback_id: Playback&#39;s id
    :type playback_id: str

    """
    return web.Response(status=200)
