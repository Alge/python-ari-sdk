# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from ari_async_sdk.models.base_model import Model
from ari_async_sdk.models.bridge import Bridge
from ari_async_sdk.models.channel import Channel
from ari_async_sdk.models.event import Event
from ari_async_sdk import util


class BridgeBlindTransfer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, application: str=None, timestamp: date=None, asterisk_id: str=None, type: str=None, bridge: Bridge=None, channel: Channel=None, context: str=None, exten: str=None, is_external: bool=None, replace_channel: Channel=None, result: str=None, transferee: Channel=None):
        """BridgeBlindTransfer - a model defined in OpenAPI

        :param application: The application of this BridgeBlindTransfer.
        :param timestamp: The timestamp of this BridgeBlindTransfer.
        :param asterisk_id: The asterisk_id of this BridgeBlindTransfer.
        :param type: The type of this BridgeBlindTransfer.
        :param bridge: The bridge of this BridgeBlindTransfer.
        :param channel: The channel of this BridgeBlindTransfer.
        :param context: The context of this BridgeBlindTransfer.
        :param exten: The exten of this BridgeBlindTransfer.
        :param is_external: The is_external of this BridgeBlindTransfer.
        :param replace_channel: The replace_channel of this BridgeBlindTransfer.
        :param result: The result of this BridgeBlindTransfer.
        :param transferee: The transferee of this BridgeBlindTransfer.
        """
        self.openapi_types = {
            'application': str,
            'timestamp': date,
            'asterisk_id': str,
            'type': str,
            'bridge': Bridge,
            'channel': Channel,
            'context': str,
            'exten': str,
            'is_external': bool,
            'replace_channel': Channel,
            'result': str,
            'transferee': Channel
        }

        self.attribute_map = {
            'application': 'application',
            'timestamp': 'timestamp',
            'asterisk_id': 'asterisk_id',
            'type': 'type',
            'bridge': 'bridge',
            'channel': 'channel',
            'context': 'context',
            'exten': 'exten',
            'is_external': 'is_external',
            'replace_channel': 'replace_channel',
            'result': 'result',
            'transferee': 'transferee'
        }

        self._application = application
        self._timestamp = timestamp
        self._asterisk_id = asterisk_id
        self._type = type
        self._bridge = bridge
        self._channel = channel
        self._context = context
        self._exten = exten
        self._is_external = is_external
        self._replace_channel = replace_channel
        self._result = result
        self._transferee = transferee

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BridgeBlindTransfer':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BridgeBlindTransfer of this BridgeBlindTransfer.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application(self):
        """Gets the application of this BridgeBlindTransfer.

        Name of the application receiving the event.

        :return: The application of this BridgeBlindTransfer.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this BridgeBlindTransfer.

        Name of the application receiving the event.

        :param application: The application of this BridgeBlindTransfer.
        :type application: str
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")

        self._application = application

    @property
    def timestamp(self):
        """Gets the timestamp of this BridgeBlindTransfer.

        Time at which this event was created.

        :return: The timestamp of this BridgeBlindTransfer.
        :rtype: date
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BridgeBlindTransfer.

        Time at which this event was created.

        :param timestamp: The timestamp of this BridgeBlindTransfer.
        :type timestamp: date
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def asterisk_id(self):
        """Gets the asterisk_id of this BridgeBlindTransfer.

        The unique ID for the Asterisk instance that raised this event.

        :return: The asterisk_id of this BridgeBlindTransfer.
        :rtype: str
        """
        return self._asterisk_id

    @asterisk_id.setter
    def asterisk_id(self, asterisk_id):
        """Sets the asterisk_id of this BridgeBlindTransfer.

        The unique ID for the Asterisk instance that raised this event.

        :param asterisk_id: The asterisk_id of this BridgeBlindTransfer.
        :type asterisk_id: str
        """

        self._asterisk_id = asterisk_id

    @property
    def type(self):
        """Gets the type of this BridgeBlindTransfer.

        Indicates the type of this message.

        :return: The type of this BridgeBlindTransfer.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BridgeBlindTransfer.

        Indicates the type of this message.

        :param type: The type of this BridgeBlindTransfer.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def bridge(self):
        """Gets the bridge of this BridgeBlindTransfer.


        :return: The bridge of this BridgeBlindTransfer.
        :rtype: Bridge
        """
        return self._bridge

    @bridge.setter
    def bridge(self, bridge):
        """Sets the bridge of this BridgeBlindTransfer.


        :param bridge: The bridge of this BridgeBlindTransfer.
        :type bridge: Bridge
        """

        self._bridge = bridge

    @property
    def channel(self):
        """Gets the channel of this BridgeBlindTransfer.


        :return: The channel of this BridgeBlindTransfer.
        :rtype: Channel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this BridgeBlindTransfer.


        :param channel: The channel of this BridgeBlindTransfer.
        :type channel: Channel
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")

        self._channel = channel

    @property
    def context(self):
        """Gets the context of this BridgeBlindTransfer.

        The context transferred to

        :return: The context of this BridgeBlindTransfer.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this BridgeBlindTransfer.

        The context transferred to

        :param context: The context of this BridgeBlindTransfer.
        :type context: str
        """
        if context is None:
            raise ValueError("Invalid value for `context`, must not be `None`")

        self._context = context

    @property
    def exten(self):
        """Gets the exten of this BridgeBlindTransfer.

        The extension transferred to

        :return: The exten of this BridgeBlindTransfer.
        :rtype: str
        """
        return self._exten

    @exten.setter
    def exten(self, exten):
        """Sets the exten of this BridgeBlindTransfer.

        The extension transferred to

        :param exten: The exten of this BridgeBlindTransfer.
        :type exten: str
        """
        if exten is None:
            raise ValueError("Invalid value for `exten`, must not be `None`")

        self._exten = exten

    @property
    def is_external(self):
        """Gets the is_external of this BridgeBlindTransfer.

        Whether the transfer was externally initiated or not

        :return: The is_external of this BridgeBlindTransfer.
        :rtype: bool
        """
        return self._is_external

    @is_external.setter
    def is_external(self, is_external):
        """Sets the is_external of this BridgeBlindTransfer.

        Whether the transfer was externally initiated or not

        :param is_external: The is_external of this BridgeBlindTransfer.
        :type is_external: bool
        """
        if is_external is None:
            raise ValueError("Invalid value for `is_external`, must not be `None`")

        self._is_external = is_external

    @property
    def replace_channel(self):
        """Gets the replace_channel of this BridgeBlindTransfer.


        :return: The replace_channel of this BridgeBlindTransfer.
        :rtype: Channel
        """
        return self._replace_channel

    @replace_channel.setter
    def replace_channel(self, replace_channel):
        """Sets the replace_channel of this BridgeBlindTransfer.


        :param replace_channel: The replace_channel of this BridgeBlindTransfer.
        :type replace_channel: Channel
        """

        self._replace_channel = replace_channel

    @property
    def result(self):
        """Gets the result of this BridgeBlindTransfer.

        The result of the transfer attempt

        :return: The result of this BridgeBlindTransfer.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this BridgeBlindTransfer.

        The result of the transfer attempt

        :param result: The result of this BridgeBlindTransfer.
        :type result: str
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")

        self._result = result

    @property
    def transferee(self):
        """Gets the transferee of this BridgeBlindTransfer.


        :return: The transferee of this BridgeBlindTransfer.
        :rtype: Channel
        """
        return self._transferee

    @transferee.setter
    def transferee(self, transferee):
        """Sets the transferee of this BridgeBlindTransfer.


        :param transferee: The transferee of this BridgeBlindTransfer.
        :type transferee: Channel
        """

        self._transferee = transferee
