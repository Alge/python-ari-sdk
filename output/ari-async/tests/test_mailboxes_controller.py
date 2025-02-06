# coding: utf-8

import pytest
import json
from aiohttp import web

from ari_async_sdk.models.mailbox import Mailbox


pytestmark = pytest.mark.asyncio

async def test_deletemailbox(client):
    """Test case for deletemailbox

    Destroy a mailbox.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ari/mailboxes/{mailbox_name}'.format(mailbox_name='mailbox_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getmailbox(client):
    """Test case for getmailbox

    Retrieve the current state of a mailbox.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/mailboxes/{mailbox_name}'.format(mailbox_name='mailbox_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listmailboxes(client):
    """Test case for listmailboxes

    List all mailboxes.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ari/mailboxes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updatemailbox(client):
    """Test case for updatemailbox

    Change the state of a mailbox. (Note - implicitly creates the mailbox).
    """
    params = [('oldMessages', 56),
                    ('newMessages', 56)]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/ari/mailboxes/{mailbox_name}'.format(mailbox_name='mailbox_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

