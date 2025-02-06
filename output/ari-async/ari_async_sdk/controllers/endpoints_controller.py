from typing import List, Dict
from aiohttp import web

from ari_async_sdk.models.endpoint import Endpoint
from ari_async_sdk import util


async def getendpoint(request: web.Request, tech, resource) -> web.Response:
    """Details for an endpoint.

    

    :param tech: Technology of the endpoint
    :type tech: str
    :param resource: ID of the endpoint
    :type resource: str

    """
    return web.Response(status=200)


async def list_by_tech(request: web.Request, tech) -> web.Response:
    """List available endoints for a given endpoint technology.

    

    :param tech: Technology of the endpoints (sip,iax2,...)
    :type tech: str

    """
    return web.Response(status=200)


async def listendpoints(request: web.Request, ) -> web.Response:
    """List all endpoints.

    


    """
    return web.Response(status=200)


async def send_message(request: web.Request, to, _from, body=None, variables=None) -> web.Response:
    """Send a message to some technology URI or endpoint.

    

    :param to: The endpoint resource or technology specific URI to send the message to. Valid resources are sip, pjsip, and xmpp.
    :type to: str
    :param _from: The endpoint resource or technology specific identity to send this message from. Valid resources are sip, pjsip, and xmpp.
    :type _from: str
    :param body: The body of the message
    :type body: str
    :param variables: 
    :type variables: 

    """
    return web.Response(status=200)


async def send_message_to_endpoint(request: web.Request, tech, resource, _from, body=None, variables=None) -> web.Response:
    """Send a message to some endpoint in a technology.

    

    :param tech: Technology of the endpoint
    :type tech: str
    :param resource: ID of the endpoint
    :type resource: str
    :param _from: The endpoint resource or technology specific identity to send this message from. Valid resources are sip, pjsip, and xmpp.
    :type _from: str
    :param body: The body of the message
    :type body: str
    :param variables: 
    :type variables: 

    """
    return web.Response(status=200)
