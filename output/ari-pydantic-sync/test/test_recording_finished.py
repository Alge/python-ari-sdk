# coding: utf-8

"""
    Asterisk ARI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from ari_sync_sdk.models.recording_finished import RecordingFinished  # noqa: E501

class TestRecordingFinished(unittest.TestCase):
    """RecordingFinished unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecordingFinished:
        """Test RecordingFinished
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecordingFinished`
        """
        model = RecordingFinished()  # noqa: E501
        if include_optional:
            return RecordingFinished(
                recording = ari_sync_sdk.models.live_recording.LiveRecording(
                    cause = '', 
                    duration = 56, 
                    format = '', 
                    name = '', 
                    silence_duration = 56, 
                    state = '', 
                    talking_duration = 56, 
                    target_uri = '', )
            )
        else:
            return RecordingFinished(
                recording = ari_sync_sdk.models.live_recording.LiveRecording(
                    cause = '', 
                    duration = 56, 
                    format = '', 
                    name = '', 
                    silence_duration = 56, 
                    state = '', 
                    talking_duration = 56, 
                    target_uri = '', ),
        )
        """

    def testRecordingFinished(self):
        """Test RecordingFinished"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
