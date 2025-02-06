# coding: utf-8

"""
    Asterisk ARI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ari_async_sdk.api.endpoints_api import EndpointsApi  # noqa: E501


class TestEndpointsApi(unittest.IsolatedAsyncioTestCase):
    """EndpointsApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = EndpointsApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_getendpoint(self) -> None:
        """Test case for getendpoint

        Details for an endpoint.  # noqa: E501
        """
        pass

    async def test_list_by_tech(self) -> None:
        """Test case for list_by_tech

        List available endoints for a given endpoint technology.  # noqa: E501
        """
        pass

    async def test_listendpoints(self) -> None:
        """Test case for listendpoints

        List all endpoints.  # noqa: E501
        """
        pass

    async def test_send_message(self) -> None:
        """Test case for send_message

        Send a message to some technology URI or endpoint.  # noqa: E501
        """
        pass

    async def test_send_message_to_endpoint(self) -> None:
        """Test case for send_message_to_endpoint

        Send a message to some endpoint in a technology.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
