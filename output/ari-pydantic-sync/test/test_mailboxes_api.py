# coding: utf-8

"""
    Asterisk ARI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ari_sync_sdk.api.mailboxes_api import MailboxesApi  # noqa: E501


class TestMailboxesApi(unittest.TestCase):
    """MailboxesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MailboxesApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_deletemailbox(self) -> None:
        """Test case for deletemailbox

        Destroy a mailbox.  # noqa: E501
        """
        pass

    def test_getmailbox(self) -> None:
        """Test case for getmailbox

        Retrieve the current state of a mailbox.  # noqa: E501
        """
        pass

    def test_listmailboxes(self) -> None:
        """Test case for listmailboxes

        List all mailboxes.  # noqa: E501
        """
        pass

    def test_updatemailbox(self) -> None:
        """Test case for updatemailbox

        Change the state of a mailbox. (Note - implicitly creates the mailbox).  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
