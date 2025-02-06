# coding: utf-8

"""
    Asterisk ARI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ari_sync_sdk.api.device_states_api import DeviceStatesApi  # noqa: E501


class TestDeviceStatesApi(unittest.IsolatedAsyncioTestCase):
    """DeviceStatesApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = DeviceStatesApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_delete(self) -> None:
        """Test case for delete

        Destroy a device-state controlled by ARI.  # noqa: E501
        """
        pass

    async def test_getdevicestate(self) -> None:
        """Test case for getdevicestate

        Retrieve the current state of a device.  # noqa: E501
        """
        pass

    async def test_list_device_states(self) -> None:
        """Test case for list_device_states

        List all ARI controlled device states.  # noqa: E501
        """
        pass

    async def test_update(self) -> None:
        """Test case for update

        Change the state of a device controlled by ARI. (Note - implicitly creates the device state).  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
