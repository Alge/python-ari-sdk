from typing import List, Dict
from aiohttp import web

from ari_async_sdk.models.live_recording import LiveRecording
from ari_async_sdk.models.stored_recording import StoredRecording
from ari_async_sdk import util


async def cancel(request: web.Request, recording_name) -> web.Response:
    """Stop a live recording and discard it.

    

    :param recording_name: The name of the recording
    :type recording_name: str

    """
    return web.Response(status=200)


async def copy_stored(request: web.Request, recording_name, destination_recording_name) -> web.Response:
    """Copy a stored recording.

    

    :param recording_name: The name of the recording to copy
    :type recording_name: str
    :param destination_recording_name: The destination name of the recording
    :type destination_recording_name: str

    """
    return web.Response(status=200)


async def delete_stored(request: web.Request, recording_name) -> web.Response:
    """Delete a stored recording.

    

    :param recording_name: The name of the recording
    :type recording_name: str

    """
    return web.Response(status=200)


async def get_live(request: web.Request, recording_name) -> web.Response:
    """List live recordings.

    

    :param recording_name: The name of the recording
    :type recording_name: str

    """
    return web.Response(status=200)


async def get_stored(request: web.Request, recording_name) -> web.Response:
    """Get a stored recording&#39;s details.

    

    :param recording_name: The name of the recording
    :type recording_name: str

    """
    return web.Response(status=200)


async def get_stored_file(request: web.Request, recording_name) -> web.Response:
    """Get the file associated with the stored recording.

    

    :param recording_name: The name of the recording
    :type recording_name: str

    """
    return web.Response(status=200)


async def list_stored(request: web.Request, ) -> web.Response:
    """List recordings that are complete.

    


    """
    return web.Response(status=200)


async def muterecording(request: web.Request, recording_name) -> web.Response:
    """Mute a live recording.

    Muting a recording suspends silence detection, which will be restarted when the recording is unmuted.

    :param recording_name: The name of the recording
    :type recording_name: str

    """
    return web.Response(status=200)


async def pause(request: web.Request, recording_name) -> web.Response:
    """Pause a live recording.

    Pausing a recording suspends silence detection, which will be restarted when the recording is unpaused. Paused time is not included in the accounting for maxDurationSeconds.

    :param recording_name: The name of the recording
    :type recording_name: str

    """
    return web.Response(status=200)


async def stoprecording(request: web.Request, recording_name) -> web.Response:
    """Stop a live recording and store it.

    

    :param recording_name: The name of the recording
    :type recording_name: str

    """
    return web.Response(status=200)


async def unmuterecording(request: web.Request, recording_name) -> web.Response:
    """Unmute a live recording.

    

    :param recording_name: The name of the recording
    :type recording_name: str

    """
    return web.Response(status=200)


async def unpause(request: web.Request, recording_name) -> web.Response:
    """Unpause a live recording.

    

    :param recording_name: The name of the recording
    :type recording_name: str

    """
    return web.Response(status=200)
