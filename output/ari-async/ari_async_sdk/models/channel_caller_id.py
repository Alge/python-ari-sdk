# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from ari_async_sdk.models.base_model import Model
from ari_async_sdk.models.channel import Channel
from ari_async_sdk.models.event import Event
from ari_async_sdk import util


class ChannelCallerId(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, application: str=None, timestamp: date=None, asterisk_id: str=None, type: str=None, caller_presentation: int=None, caller_presentation_txt: str=None, channel: Channel=None):
        """ChannelCallerId - a model defined in OpenAPI

        :param application: The application of this ChannelCallerId.
        :param timestamp: The timestamp of this ChannelCallerId.
        :param asterisk_id: The asterisk_id of this ChannelCallerId.
        :param type: The type of this ChannelCallerId.
        :param caller_presentation: The caller_presentation of this ChannelCallerId.
        :param caller_presentation_txt: The caller_presentation_txt of this ChannelCallerId.
        :param channel: The channel of this ChannelCallerId.
        """
        self.openapi_types = {
            'application': str,
            'timestamp': date,
            'asterisk_id': str,
            'type': str,
            'caller_presentation': int,
            'caller_presentation_txt': str,
            'channel': Channel
        }

        self.attribute_map = {
            'application': 'application',
            'timestamp': 'timestamp',
            'asterisk_id': 'asterisk_id',
            'type': 'type',
            'caller_presentation': 'caller_presentation',
            'caller_presentation_txt': 'caller_presentation_txt',
            'channel': 'channel'
        }

        self._application = application
        self._timestamp = timestamp
        self._asterisk_id = asterisk_id
        self._type = type
        self._caller_presentation = caller_presentation
        self._caller_presentation_txt = caller_presentation_txt
        self._channel = channel

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ChannelCallerId':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ChannelCallerId of this ChannelCallerId.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application(self):
        """Gets the application of this ChannelCallerId.

        Name of the application receiving the event.

        :return: The application of this ChannelCallerId.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this ChannelCallerId.

        Name of the application receiving the event.

        :param application: The application of this ChannelCallerId.
        :type application: str
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")

        self._application = application

    @property
    def timestamp(self):
        """Gets the timestamp of this ChannelCallerId.

        Time at which this event was created.

        :return: The timestamp of this ChannelCallerId.
        :rtype: date
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ChannelCallerId.

        Time at which this event was created.

        :param timestamp: The timestamp of this ChannelCallerId.
        :type timestamp: date
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def asterisk_id(self):
        """Gets the asterisk_id of this ChannelCallerId.

        The unique ID for the Asterisk instance that raised this event.

        :return: The asterisk_id of this ChannelCallerId.
        :rtype: str
        """
        return self._asterisk_id

    @asterisk_id.setter
    def asterisk_id(self, asterisk_id):
        """Sets the asterisk_id of this ChannelCallerId.

        The unique ID for the Asterisk instance that raised this event.

        :param asterisk_id: The asterisk_id of this ChannelCallerId.
        :type asterisk_id: str
        """

        self._asterisk_id = asterisk_id

    @property
    def type(self):
        """Gets the type of this ChannelCallerId.

        Indicates the type of this message.

        :return: The type of this ChannelCallerId.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChannelCallerId.

        Indicates the type of this message.

        :param type: The type of this ChannelCallerId.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def caller_presentation(self):
        """Gets the caller_presentation of this ChannelCallerId.

        The integer representation of the Caller Presentation value.

        :return: The caller_presentation of this ChannelCallerId.
        :rtype: int
        """
        return self._caller_presentation

    @caller_presentation.setter
    def caller_presentation(self, caller_presentation):
        """Sets the caller_presentation of this ChannelCallerId.

        The integer representation of the Caller Presentation value.

        :param caller_presentation: The caller_presentation of this ChannelCallerId.
        :type caller_presentation: int
        """
        if caller_presentation is None:
            raise ValueError("Invalid value for `caller_presentation`, must not be `None`")

        self._caller_presentation = caller_presentation

    @property
    def caller_presentation_txt(self):
        """Gets the caller_presentation_txt of this ChannelCallerId.

        The text representation of the Caller Presentation value.

        :return: The caller_presentation_txt of this ChannelCallerId.
        :rtype: str
        """
        return self._caller_presentation_txt

    @caller_presentation_txt.setter
    def caller_presentation_txt(self, caller_presentation_txt):
        """Sets the caller_presentation_txt of this ChannelCallerId.

        The text representation of the Caller Presentation value.

        :param caller_presentation_txt: The caller_presentation_txt of this ChannelCallerId.
        :type caller_presentation_txt: str
        """
        if caller_presentation_txt is None:
            raise ValueError("Invalid value for `caller_presentation_txt`, must not be `None`")

        self._caller_presentation_txt = caller_presentation_txt

    @property
    def channel(self):
        """Gets the channel of this ChannelCallerId.


        :return: The channel of this ChannelCallerId.
        :rtype: Channel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ChannelCallerId.


        :param channel: The channel of this ChannelCallerId.
        :type channel: Channel
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")

        self._channel = channel
