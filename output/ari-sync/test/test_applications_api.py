# coding: utf-8

"""
    Asterisk ARI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ari_sync_sdk.api.applications_api import ApplicationsApi


class TestApplicationsApi(unittest.TestCase):
    """ApplicationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ApplicationsApi()

    def tearDown(self) -> None:
        pass

    def test_filter(self) -> None:
        """Test case for filter

        Filter application events types.
        """
        pass

    def test_get(self) -> None:
        """Test case for get

        Get details of an application.
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        List all applications.
        """
        pass

    def test_subscribe(self) -> None:
        """Test case for subscribe

        Subscribe an application to a event source.
        """
        pass

    def test_unsubscribe(self) -> None:
        """Test case for unsubscribe

        Unsubscribe an application from an event source.
        """
        pass


if __name__ == '__main__':
    unittest.main()
