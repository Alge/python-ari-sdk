from typing import List, Dict
from aiohttp import web

from ari_async_sdk.models.bridge import Bridge
from ari_async_sdk.models.live_recording import LiveRecording
from ari_async_sdk.models.playback import Playback
from ari_async_sdk import util


async def add_channel(request: web.Request, bridge_id, channel, role=None, absorb_dtmf=None, mute=None, inhibit_connected_line_updates=None) -> web.Response:
    """Add a channel to a bridge.

    

    :param bridge_id: Bridge&#39;s id
    :type bridge_id: str
    :param channel: Ids of channels to add to bridge
    :type channel: List[str]
    :param role: Channel&#39;s role in the bridge
    :type role: str
    :param absorb_dtmf: Absorb DTMF coming from this channel, preventing it to pass through to the bridge
    :type absorb_dtmf: bool
    :param mute: Mute audio from this channel, preventing it to pass through to the bridge
    :type mute: bool
    :param inhibit_connected_line_updates: Do not present the identity of the newly connected channel to other bridge members
    :type inhibit_connected_line_updates: bool

    """
    return web.Response(status=200)


async def clear_video_source(request: web.Request, bridge_id) -> web.Response:
    """Removes any explicit video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants. When no explicit video source is set, talk detection will be used to determine the active video stream.

    

    :param bridge_id: Bridge&#39;s id
    :type bridge_id: str

    """
    return web.Response(status=200)


async def create(request: web.Request, type=None, bridge_id=None, name=None) -> web.Response:
    """Create a new bridge.

    This bridge persists until it has been shut down, or Asterisk has been shut down.

    :param type: Comma separated list of bridge type attributes (mixing, holding, dtmf_events, proxy_media, video_sfu).
    :type type: str
    :param bridge_id: Unique ID to give to the bridge being created.
    :type bridge_id: str
    :param name: Name to give to the bridge being created.
    :type name: str

    """
    return web.Response(status=200)


async def create_with_id(request: web.Request, bridge_id, type=None, name=None) -> web.Response:
    """Create a new bridge or updates an existing one.

    This bridge persists until it has been shut down, or Asterisk has been shut down.

    :param bridge_id: Unique ID to give to the bridge being created.
    :type bridge_id: str
    :param type: Comma separated list of bridge type attributes (mixing, holding, dtmf_events, proxy_media, video_sfu) to set.
    :type type: str
    :param name: Set the name of the bridge.
    :type name: str

    """
    return web.Response(status=200)


async def destroy(request: web.Request, bridge_id) -> web.Response:
    """Shut down a bridge.

    If any channels are in this bridge, they will be removed and resume whatever they were doing beforehand.

    :param bridge_id: Bridge&#39;s id
    :type bridge_id: str

    """
    return web.Response(status=200)


async def getbridge(request: web.Request, bridge_id) -> web.Response:
    """Get bridge details.

    

    :param bridge_id: Bridge&#39;s id
    :type bridge_id: str

    """
    return web.Response(status=200)


async def listbridges(request: web.Request, ) -> web.Response:
    """List all active bridges in Asterisk.

    


    """
    return web.Response(status=200)


async def play(request: web.Request, bridge_id, media, lang=None, offsetms=None, skipms=None, playback_id=None) -> web.Response:
    """Start playback of media on a bridge.

    The media URI may be any of a number of URI&#39;s. Currently sound:, recording:, number:, digits:, characters:, and tone: URI&#39;s are supported. This operation creates a playback resource that can be used to control the playback of media (pause, rewind, fast forward, etc.)

    :param bridge_id: Bridge&#39;s id
    :type bridge_id: str
    :param media: Media URIs to play.
    :type media: List[str]
    :param lang: For sounds, selects language for sound.
    :type lang: str
    :param offsetms: Number of milliseconds to skip before playing. Only applies to the first URI if multiple media URIs are specified.
    :type offsetms: int
    :param skipms: Number of milliseconds to skip for forward/reverse operations.
    :type skipms: int
    :param playback_id: Playback Id.
    :type playback_id: str

    """
    return web.Response(status=200)


async def play_with_id(request: web.Request, bridge_id, playback_id, media, lang=None, offsetms=None, skipms=None) -> web.Response:
    """Start playback of media on a bridge.

    The media URI may be any of a number of URI&#39;s. Currently sound:, recording:, number:, digits:, characters:, and tone: URI&#39;s are supported. This operation creates a playback resource that can be used to control the playback of media (pause, rewind, fast forward, etc.)

    :param bridge_id: Bridge&#39;s id
    :type bridge_id: str
    :param playback_id: Playback ID.
    :type playback_id: str
    :param media: Media URIs to play.
    :type media: List[str]
    :param lang: For sounds, selects language for sound.
    :type lang: str
    :param offsetms: Number of milliseconds to skip before playing. Only applies to the first URI if multiple media URIs are specified.
    :type offsetms: int
    :param skipms: Number of milliseconds to skip for forward/reverse operations.
    :type skipms: int

    """
    return web.Response(status=200)


async def record(request: web.Request, bridge_id, name, format, max_duration_seconds=None, max_silence_seconds=None, if_exists=None, beep=None, terminate_on=None) -> web.Response:
    """Start a recording.

    This records the mixed audio from all channels participating in this bridge.

    :param bridge_id: Bridge&#39;s id
    :type bridge_id: str
    :param name: Recording&#39;s filename
    :type name: str
    :param format: Format to encode audio in
    :type format: str
    :param max_duration_seconds: Maximum duration of the recording, in seconds. 0 for no limit.
    :type max_duration_seconds: int
    :param max_silence_seconds: Maximum duration of silence, in seconds. 0 for no limit.
    :type max_silence_seconds: int
    :param if_exists: Action to take if a recording with the same name already exists.
    :type if_exists: str
    :param beep: Play beep when recording begins
    :type beep: bool
    :param terminate_on: DTMF input to terminate recording.
    :type terminate_on: str

    """
    return web.Response(status=200)


async def remove_channel(request: web.Request, bridge_id, channel) -> web.Response:
    """Remove a channel from a bridge.

    

    :param bridge_id: Bridge&#39;s id
    :type bridge_id: str
    :param channel: Ids of channels to remove from bridge
    :type channel: List[str]

    """
    return web.Response(status=200)


async def set_video_source(request: web.Request, bridge_id, channel_id) -> web.Response:
    """Set a channel as the video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants.

    

    :param bridge_id: Bridge&#39;s id
    :type bridge_id: str
    :param channel_id: Channel&#39;s id
    :type channel_id: str

    """
    return web.Response(status=200)


async def start_moh(request: web.Request, bridge_id, moh_class=None) -> web.Response:
    """Play music on hold to a bridge or change the MOH class that is playing.

    

    :param bridge_id: Bridge&#39;s id
    :type bridge_id: str
    :param moh_class: Channel&#39;s id
    :type moh_class: str

    """
    return web.Response(status=200)


async def stop_moh(request: web.Request, bridge_id) -> web.Response:
    """Stop playing music on hold to a bridge.

    This will only stop music on hold being played via POST bridges/{bridgeId}/moh.

    :param bridge_id: Bridge&#39;s id
    :type bridge_id: str

    """
    return web.Response(status=200)
