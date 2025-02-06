from typing import List, Dict
from aiohttp import web

from ari_async_sdk.models.mailbox import Mailbox
from ari_async_sdk import util


async def deletemailbox(request: web.Request, mailbox_name) -> web.Response:
    """Destroy a mailbox.

    

    :param mailbox_name: Name of the mailbox
    :type mailbox_name: str

    """
    return web.Response(status=200)


async def getmailbox(request: web.Request, mailbox_name) -> web.Response:
    """Retrieve the current state of a mailbox.

    

    :param mailbox_name: Name of the mailbox
    :type mailbox_name: str

    """
    return web.Response(status=200)


async def listmailboxes(request: web.Request, ) -> web.Response:
    """List all mailboxes.

    


    """
    return web.Response(status=200)


async def updatemailbox(request: web.Request, mailbox_name, old_messages, new_messages) -> web.Response:
    """Change the state of a mailbox. (Note - implicitly creates the mailbox).

    

    :param mailbox_name: Name of the mailbox
    :type mailbox_name: str
    :param old_messages: Count of old messages in the mailbox
    :type old_messages: int
    :param new_messages: Count of new messages in the mailbox
    :type new_messages: int

    """
    return web.Response(status=200)
