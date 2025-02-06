# coding: utf-8

"""
    Asterisk ARI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ari_async_sdk.api.playbacks_api import PlaybacksApi  # noqa: E501


class TestPlaybacksApi(unittest.IsolatedAsyncioTestCase):
    """PlaybacksApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = PlaybacksApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_control(self) -> None:
        """Test case for control

        Control a playback.  # noqa: E501
        """
        pass

    async def test_getplayback(self) -> None:
        """Test case for getplayback

        Get a playback's details.  # noqa: E501
        """
        pass

    async def test_stop(self) -> None:
        """Test case for stop

        Stop a playback.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
