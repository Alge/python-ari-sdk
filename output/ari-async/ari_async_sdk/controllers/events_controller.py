from typing import List, Dict
from aiohttp import web

from ari_async_sdk.models.message import Message
from ari_async_sdk import util


async def event_websocket(request: web.Request, app, subscribe_all=None) -> web.Response:
    """WebSocket connection for events.

    

    :param app: Applications to subscribe to.
    :type app: List[str]
    :param subscribe_all: Subscribe to all Asterisk events. If provided, the applications listed will be subscribed to all events, effectively disabling the application specific subscriptions. Default is &#39;false&#39;.
    :type subscribe_all: bool

    """
    return web.Response(status=200)


async def user_event(request: web.Request, event_name, application, source=None, variables=None) -> web.Response:
    """Generate a user event.

    

    :param event_name: Event name
    :type event_name: str
    :param application: The name of the application that will receive this event
    :type application: str
    :param source: URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}/{resource}, deviceState:{deviceName}
    :type source: List[str]
    :param variables: The \&quot;variables\&quot; key in the body object holds custom key/value pairs to add to the user event. Ex. { \&quot;variables\&quot;: { \&quot;key\&quot;: \&quot;value\&quot; } }
    :type variables: 

    """
    return web.Response(status=200)
