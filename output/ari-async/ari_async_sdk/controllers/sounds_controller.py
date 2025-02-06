from typing import List, Dict
from aiohttp import web

from ari_async_sdk.models.sound import Sound
from ari_async_sdk import util


async def getsound(request: web.Request, sound_id) -> web.Response:
    """Get a sound&#39;s details.

    

    :param sound_id: Sound&#39;s id
    :type sound_id: str

    """
    return web.Response(status=200)


async def listsounds(request: web.Request, lang=None, format=None) -> web.Response:
    """List all sounds.

    

    :param lang: Lookup sound for a specific language.
    :type lang: str
    :param format: Lookup sound in a specific format.
    :type format: str

    """
    return web.Response(status=200)
