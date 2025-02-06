from typing import List, Dict
from aiohttp import web

from ari_async_sdk.models.application import Application
from ari_async_sdk import util


async def filter(request: web.Request, application_name, filter=None) -> web.Response:
    """Filter application events types.

    Allowed and/or disallowed event type filtering can be done. The body (parameter) should specify a JSON key/value object that describes the type of event filtering needed. One, or both of the following keys can be designated:&lt;br /&gt;&lt;br /&gt;\&quot;allowed\&quot; - Specifies an allowed list of event types&lt;br /&gt;\&quot;disallowed\&quot; - Specifies a disallowed list of event types&lt;br /&gt;&lt;br /&gt;Further, each of those key&#39;s value should be a JSON array that holds zero, or more JSON key/value objects. Each of these objects must contain the following key with an associated value:&lt;br /&gt;&lt;br /&gt;\&quot;type\&quot; - The type name of the event to filter&lt;br /&gt;&lt;br /&gt;The value must be the string name (case sensitive) of the event type that needs filtering. For example:&lt;br /&gt;&lt;br /&gt;{ \&quot;allowed\&quot;: [ { \&quot;type\&quot;: \&quot;StasisStart\&quot; }, { \&quot;type\&quot;: \&quot;StasisEnd\&quot; } ] }&lt;br /&gt;&lt;br /&gt;As this specifies only an allowed list, then only those two event type messages are sent to the application. No other event messages are sent.&lt;br /&gt;&lt;br /&gt;The following rules apply:&lt;br /&gt;&lt;br /&gt;* If the body is empty, both the allowed and disallowed filters are set empty.&lt;br /&gt;* If both list types are given then both are set to their respective values (note, specifying an empty array for a given type sets that type to empty).&lt;br /&gt;* If only one list type is given then only that type is set. The other type is not updated.&lt;br /&gt;* An empty \&quot;allowed\&quot; list means all events are allowed.&lt;br /&gt;* An empty \&quot;disallowed\&quot; list means no events are disallowed.&lt;br /&gt;* Disallowed events take precedence over allowed events if the event type is specified in both lists.

    :param application_name: Application&#39;s name
    :type application_name: str
    :param filter: Specify which event types to allow/disallow
    :type filter: 

    """
    return web.Response(status=200)


async def get(request: web.Request, application_name) -> web.Response:
    """Get details of an application.

    

    :param application_name: Application&#39;s name
    :type application_name: str

    """
    return web.Response(status=200)


async def list(request: web.Request, ) -> web.Response:
    """List all applications.

    


    """
    return web.Response(status=200)


async def subscribe(request: web.Request, application_name, event_source) -> web.Response:
    """Subscribe an application to a event source.

    Returns the state of the application after the subscriptions have changed

    :param application_name: Application&#39;s name
    :type application_name: str
    :param event_source: URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName}
    :type event_source: List[str]

    """
    return web.Response(status=200)


async def unsubscribe(request: web.Request, application_name, event_source) -> web.Response:
    """Unsubscribe an application from an event source.

    Returns the state of the application after the subscriptions have changed

    :param application_name: Application&#39;s name
    :type application_name: str
    :param event_source: URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName}
    :type event_source: List[str]

    """
    return web.Response(status=200)
