from typing import List, Dict
from aiohttp import web

from ari_async_sdk.models.channel import Channel
from ari_async_sdk.models.live_recording import LiveRecording
from ari_async_sdk.models.playback import Playback
from ari_async_sdk.models.rt_pstat import RTPstat
from ari_async_sdk.models.variable import Variable
from ari_async_sdk import util


async def add_moh(request: web.Request, channel_id, moh_class=None) -> web.Response:
    """Play music on hold to a channel.

    Using media operations such as /play on a channel playing MOH in this manner will suspend MOH without resuming automatically. If continuing music on hold is desired, the stasis application must reinitiate music on hold.

    :param channel_id: Channel&#39;s id
    :type channel_id: str
    :param moh_class: Music on hold class to use
    :type moh_class: str

    """
    return web.Response(status=200)


async def answer(request: web.Request, channel_id) -> web.Response:
    """Answer a channel.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str

    """
    return web.Response(status=200)


async def continue_in_dialplan(request: web.Request, channel_id, context=None, extension=None, priority=None, label=None) -> web.Response:
    """Exit application; continue execution in the dialplan.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str
    :param context: The context to continue to.
    :type context: str
    :param extension: The extension to continue to.
    :type extension: str
    :param priority: The priority to continue to.
    :type priority: int
    :param label: The label to continue to - will supersede &#39;priority&#39; if both are provided.
    :type label: str

    """
    return web.Response(status=200)


async def createchannel(request: web.Request, endpoint, app, app_args=None, channel_id=None, other_channel_id=None, originator=None, formats=None, variables=None) -> web.Response:
    """Create channel.

    

    :param endpoint: Endpoint for channel communication
    :type endpoint: str
    :param app: Stasis Application to place channel into
    :type app: str
    :param app_args: The application arguments to pass to the Stasis application provided by &#39;app&#39;. Mutually exclusive with &#39;context&#39;, &#39;extension&#39;, &#39;priority&#39;, and &#39;label&#39;.
    :type app_args: str
    :param channel_id: The unique id to assign the channel on creation.
    :type channel_id: str
    :param other_channel_id: The unique id to assign the second channel when using local channels.
    :type other_channel_id: str
    :param originator: Unique ID of the calling channel
    :type originator: str
    :param formats: The format name capability list to use if originator is not specified. Ex. \&quot;ulaw,slin16\&quot;.  Format names can be found with \&quot;core show codecs\&quot;.
    :type formats: str
    :param variables: The \&quot;variables\&quot; key in the body object holds variable key/value pairs to set on the channel on creation. Other keys in the body object are interpreted as query parameters. Ex. { \&quot;endpoint\&quot;: \&quot;SIP/Alice\&quot;, \&quot;variables\&quot;: { \&quot;CALLERID(name)\&quot;: \&quot;Alice\&quot; } }
    :type variables: 

    """
    return web.Response(status=200)


async def deletemoh(request: web.Request, channel_id) -> web.Response:
    """Stop playing music on hold to a channel.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str

    """
    return web.Response(status=200)


async def dial(request: web.Request, channel_id, caller=None, timeout=None) -> web.Response:
    """Dial a created channel.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str
    :param caller: Channel ID of caller
    :type caller: str
    :param timeout: Dial timeout
    :type timeout: int

    """
    return web.Response(status=200)


async def external_media(request: web.Request, app, external_host, format, channel_id=None, encapsulation=None, transport=None, connection_type=None, direction=None, data=None, variables=None) -> web.Response:
    """Start an External Media session.

    Create a channel to an External Media source/sink.

    :param app: Stasis Application to place channel into
    :type app: str
    :param external_host: Hostname/ip:port of external host
    :type external_host: str
    :param format: Format to encode audio in
    :type format: str
    :param channel_id: The unique id to assign the channel on creation.
    :type channel_id: str
    :param encapsulation: Payload encapsulation protocol
    :type encapsulation: str
    :param transport: Transport protocol
    :type transport: str
    :param connection_type: Connection type (client/server)
    :type connection_type: str
    :param direction: External media direction
    :type direction: str
    :param data: An arbitrary data field
    :type data: str
    :param variables: The \&quot;variables\&quot; key in the body object holds variable key/value pairs to set on the channel on creation. Other keys in the body object are interpreted as query parameters. Ex. { \&quot;endpoint\&quot;: \&quot;SIP/Alice\&quot;, \&quot;variables\&quot;: { \&quot;CALLERID(name)\&quot;: \&quot;Alice\&quot; } }
    :type variables: 

    """
    return web.Response(status=200)


async def get_channel_var(request: web.Request, channel_id, variable) -> web.Response:
    """Get the value of a channel variable or function.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str
    :param variable: The channel variable or function to get
    :type variable: str

    """
    return web.Response(status=200)


async def getchannel(request: web.Request, channel_id) -> web.Response:
    """Channel details.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str

    """
    return web.Response(status=200)


async def hangup(request: web.Request, channel_id, reason_code=None, reason=None) -> web.Response:
    """Delete (i.e. hangup) a channel.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str
    :param reason_code: The reason code for hanging up the channel for detail use. Mutually exclusive with &#39;reason&#39;. See detail hangup codes at here. https://wiki.asterisk.org/wiki/display/AST/Hangup+Cause+Mappings
    :type reason_code: str
    :param reason: Reason for hanging up the channel for simple use. Mutually exclusive with &#39;reason_code&#39;.
    :type reason: str

    """
    return web.Response(status=200)


async def hold(request: web.Request, channel_id) -> web.Response:
    """Hold a channel.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str

    """
    return web.Response(status=200)


async def listchannels(request: web.Request, ) -> web.Response:
    """List all active channels in Asterisk.

    


    """
    return web.Response(status=200)


async def move(request: web.Request, channel_id, app, app_args=None) -> web.Response:
    """Move the channel from one Stasis application to another.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str
    :param app: The channel will be passed to this Stasis application.
    :type app: str
    :param app_args: The application arguments to pass to the Stasis application provided by &#39;app&#39;.
    :type app_args: str

    """
    return web.Response(status=200)


async def mute(request: web.Request, channel_id, direction=None) -> web.Response:
    """Mute a channel.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str
    :param direction: Direction in which to mute audio
    :type direction: str

    """
    return web.Response(status=200)


async def originate(request: web.Request, endpoint, extension=None, context=None, priority=None, label=None, app=None, app_args=None, caller_id=None, timeout=None, channel_id=None, other_channel_id=None, originator=None, formats=None, variables=None) -> web.Response:
    """Create a new channel (originate).

    The new channel is created immediately and a snapshot of it returned. If a Stasis application is provided it will be automatically subscribed to the originated channel for further events and updates.

    :param endpoint: Endpoint to call.
    :type endpoint: str
    :param extension: The extension to dial after the endpoint answers. Mutually exclusive with &#39;app&#39;.
    :type extension: str
    :param context: The context to dial after the endpoint answers. If omitted, uses &#39;default&#39;. Mutually exclusive with &#39;app&#39;.
    :type context: str
    :param priority: The priority to dial after the endpoint answers. If omitted, uses 1. Mutually exclusive with &#39;app&#39;.
    :type priority: int
    :param label: The label to dial after the endpoint answers. Will supersede &#39;priority&#39; if provided. Mutually exclusive with &#39;app&#39;.
    :type label: str
    :param app: The application that is subscribed to the originated channel. When the channel is answered, it will be passed to this Stasis application. Mutually exclusive with &#39;context&#39;, &#39;extension&#39;, &#39;priority&#39;, and &#39;label&#39;.
    :type app: str
    :param app_args: The application arguments to pass to the Stasis application provided by &#39;app&#39;. Mutually exclusive with &#39;context&#39;, &#39;extension&#39;, &#39;priority&#39;, and &#39;label&#39;.
    :type app_args: str
    :param caller_id: CallerID to use when dialing the endpoint or extension.
    :type caller_id: str
    :param timeout: Timeout (in seconds) before giving up dialing, or -1 for no timeout.
    :type timeout: int
    :param channel_id: The unique id to assign the channel on creation.
    :type channel_id: str
    :param other_channel_id: The unique id to assign the second channel when using local channels.
    :type other_channel_id: str
    :param originator: The unique id of the channel which is originating this one.
    :type originator: str
    :param formats: The format name capability list to use if originator is not specified. Ex. \&quot;ulaw,slin16\&quot;.  Format names can be found with \&quot;core show codecs\&quot;.
    :type formats: str
    :param variables: The \&quot;variables\&quot; key in the body object holds variable key/value pairs to set on the channel on creation. Other keys in the body object are interpreted as query parameters. Ex. { \&quot;endpoint\&quot;: \&quot;SIP/Alice\&quot;, \&quot;variables\&quot;: { \&quot;CALLERID(name)\&quot;: \&quot;Alice\&quot; } }
    :type variables: 

    """
    return web.Response(status=200)


async def originate_with_id(request: web.Request, channel_id, endpoint, extension=None, context=None, priority=None, label=None, app=None, app_args=None, caller_id=None, timeout=None, other_channel_id=None, originator=None, formats=None, variables=None) -> web.Response:
    """Create a new channel (originate with id).

    The new channel is created immediately and a snapshot of it returned. If a Stasis application is provided it will be automatically subscribed to the originated channel for further events and updates.

    :param channel_id: The unique id to assign the channel on creation.
    :type channel_id: str
    :param endpoint: Endpoint to call.
    :type endpoint: str
    :param extension: The extension to dial after the endpoint answers. Mutually exclusive with &#39;app&#39;.
    :type extension: str
    :param context: The context to dial after the endpoint answers. If omitted, uses &#39;default&#39;. Mutually exclusive with &#39;app&#39;.
    :type context: str
    :param priority: The priority to dial after the endpoint answers. If omitted, uses 1. Mutually exclusive with &#39;app&#39;.
    :type priority: int
    :param label: The label to dial after the endpoint answers. Will supersede &#39;priority&#39; if provided. Mutually exclusive with &#39;app&#39;.
    :type label: str
    :param app: The application that is subscribed to the originated channel. When the channel is answered, it will be passed to this Stasis application. Mutually exclusive with &#39;context&#39;, &#39;extension&#39;, &#39;priority&#39;, and &#39;label&#39;.
    :type app: str
    :param app_args: The application arguments to pass to the Stasis application provided by &#39;app&#39;. Mutually exclusive with &#39;context&#39;, &#39;extension&#39;, &#39;priority&#39;, and &#39;label&#39;.
    :type app_args: str
    :param caller_id: CallerID to use when dialing the endpoint or extension.
    :type caller_id: str
    :param timeout: Timeout (in seconds) before giving up dialing, or -1 for no timeout.
    :type timeout: int
    :param other_channel_id: The unique id to assign the second channel when using local channels.
    :type other_channel_id: str
    :param originator: The unique id of the channel which is originating this one.
    :type originator: str
    :param formats: The format name capability list to use if originator is not specified. Ex. \&quot;ulaw,slin16\&quot;.  Format names can be found with \&quot;core show codecs\&quot;.
    :type formats: str
    :param variables: The \&quot;variables\&quot; key in the body object holds variable key/value pairs to set on the channel on creation. Other keys in the body object are interpreted as query parameters. Ex. { \&quot;endpoint\&quot;: \&quot;SIP/Alice\&quot;, \&quot;variables\&quot;: { \&quot;CALLERID(name)\&quot;: \&quot;Alice\&quot; } }
    :type variables: 

    """
    return web.Response(status=200)


async def play_sound_with_id(request: web.Request, channel_id, playback_id, media, lang=None, offsetms=None, skipms=None) -> web.Response:
    """Start playback of media and specify the playbackId.

    The media URI may be any of a number of URI&#39;s. Currently sound:, recording:, number:, digits:, characters:, and tone: URI&#39;s are supported. This operation creates a playback resource that can be used to control the playback of media (pause, rewind, fast forward, etc.)

    :param channel_id: Channel&#39;s id
    :type channel_id: str
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


async def playsound(request: web.Request, channel_id, media, lang=None, offsetms=None, skipms=None, playback_id=None) -> web.Response:
    """Start playback of media.

    The media URI may be any of a number of URI&#39;s. Currently sound:, recording:, number:, digits:, characters:, and tone: URI&#39;s are supported. This operation creates a playback resource that can be used to control the playback of media (pause, rewind, fast forward, etc.)

    :param channel_id: Channel&#39;s id
    :type channel_id: str
    :param media: Media URIs to play.
    :type media: List[str]
    :param lang: For sounds, selects language for sound.
    :type lang: str
    :param offsetms: Number of milliseconds to skip before playing. Only applies to the first URI if multiple media URIs are specified.
    :type offsetms: int
    :param skipms: Number of milliseconds to skip for forward/reverse operations.
    :type skipms: int
    :param playback_id: Playback ID.
    :type playback_id: str

    """
    return web.Response(status=200)


async def recordchannel(request: web.Request, channel_id, name, format, max_duration_seconds=None, max_silence_seconds=None, if_exists=None, beep=None, terminate_on=None) -> web.Response:
    """Start a recording.

    Record audio from a channel. Note that this will not capture audio sent to the channel. The bridge itself has a record feature if that&#39;s what you want.

    :param channel_id: Channel&#39;s id
    :type channel_id: str
    :param name: Recording&#39;s filename
    :type name: str
    :param format: Format to encode audio in
    :type format: str
    :param max_duration_seconds: Maximum duration of the recording, in seconds. 0 for no limit
    :type max_duration_seconds: int
    :param max_silence_seconds: Maximum duration of silence, in seconds. 0 for no limit
    :type max_silence_seconds: int
    :param if_exists: Action to take if a recording with the same name already exists.
    :type if_exists: str
    :param beep: Play beep when recording begins
    :type beep: bool
    :param terminate_on: DTMF input to terminate recording
    :type terminate_on: str

    """
    return web.Response(status=200)


async def redirect(request: web.Request, channel_id, endpoint) -> web.Response:
    """Redirect the channel to a different location.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str
    :param endpoint: The endpoint to redirect the channel to
    :type endpoint: str

    """
    return web.Response(status=200)


async def ring(request: web.Request, channel_id) -> web.Response:
    """Indicate ringing to a channel.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str

    """
    return web.Response(status=200)


async def ring_stop(request: web.Request, channel_id) -> web.Response:
    """Stop ringing indication on a channel if locally generated.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str

    """
    return web.Response(status=200)


async def rtpstatistics(request: web.Request, channel_id) -> web.Response:
    """RTP stats on a channel.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str

    """
    return web.Response(status=200)


async def send_dtmf(request: web.Request, channel_id, dtmf=None, before=None, between=None, duration=None, after=None) -> web.Response:
    """Send provided DTMF to a given channel.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str
    :param dtmf: DTMF To send.
    :type dtmf: str
    :param before: Amount of time to wait before DTMF digits (specified in milliseconds) start.
    :type before: int
    :param between: Amount of time in between DTMF digits (specified in milliseconds).
    :type between: int
    :param duration: Length of each DTMF digit (specified in milliseconds).
    :type duration: int
    :param after: Amount of time to wait after DTMF digits (specified in milliseconds) end.
    :type after: int

    """
    return web.Response(status=200)


async def set_channel_var(request: web.Request, channel_id, variable, value=None) -> web.Response:
    """Set the value of a channel variable or function.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str
    :param variable: The channel variable or function to set
    :type variable: str
    :param value: The value to set the variable to
    :type value: str

    """
    return web.Response(status=200)


async def snoop_channel(request: web.Request, channel_id, app, spy=None, whisper=None, app_args=None, snoop_id=None) -> web.Response:
    """Start snooping.

    Snoop (spy/whisper) on a specific channel.

    :param channel_id: Channel&#39;s id
    :type channel_id: str
    :param app: Application the snooping channel is placed into
    :type app: str
    :param spy: Direction of audio to spy on
    :type spy: str
    :param whisper: Direction of audio to whisper into
    :type whisper: str
    :param app_args: The application arguments to pass to the Stasis application
    :type app_args: str
    :param snoop_id: Unique ID to assign to snooping channel
    :type snoop_id: str

    """
    return web.Response(status=200)


async def snoop_channel_with_id(request: web.Request, channel_id, snoop_id, app, spy=None, whisper=None, app_args=None) -> web.Response:
    """Start snooping.

    Snoop (spy/whisper) on a specific channel.

    :param channel_id: Channel&#39;s id
    :type channel_id: str
    :param snoop_id: Unique ID to assign to snooping channel
    :type snoop_id: str
    :param app: Application the snooping channel is placed into
    :type app: str
    :param spy: Direction of audio to spy on
    :type spy: str
    :param whisper: Direction of audio to whisper into
    :type whisper: str
    :param app_args: The application arguments to pass to the Stasis application
    :type app_args: str

    """
    return web.Response(status=200)


async def start_silence(request: web.Request, channel_id) -> web.Response:
    """Play silence to a channel.

    Using media operations such as /play on a channel playing silence in this manner will suspend silence without resuming automatically.

    :param channel_id: Channel&#39;s id
    :type channel_id: str

    """
    return web.Response(status=200)


async def stop_silence(request: web.Request, channel_id) -> web.Response:
    """Stop playing silence to a channel.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str

    """
    return web.Response(status=200)


async def unhold(request: web.Request, channel_id) -> web.Response:
    """Remove a channel from hold.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str

    """
    return web.Response(status=200)


async def unmute(request: web.Request, channel_id, direction=None) -> web.Response:
    """Unmute a channel.

    

    :param channel_id: Channel&#39;s id
    :type channel_id: str
    :param direction: Direction in which to unmute audio
    :type direction: str

    """
    return web.Response(status=200)
