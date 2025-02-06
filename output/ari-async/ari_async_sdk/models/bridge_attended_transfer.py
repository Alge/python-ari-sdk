# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from ari_async_sdk.models.base_model import Model
from ari_async_sdk.models.bridge import Bridge
from ari_async_sdk.models.channel import Channel
from ari_async_sdk.models.event import Event
from ari_async_sdk import util


class BridgeAttendedTransfer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, application: str=None, timestamp: date=None, asterisk_id: str=None, type: str=None, destination_application: str=None, destination_bridge: str=None, destination_link_first_leg: Channel=None, destination_link_second_leg: Channel=None, destination_threeway_bridge: Bridge=None, destination_threeway_channel: Channel=None, destination_type: str=None, is_external: bool=None, replace_channel: Channel=None, result: str=None, transfer_target: Channel=None, transferee: Channel=None, transferer_first_leg: Channel=None, transferer_first_leg_bridge: Bridge=None, transferer_second_leg: Channel=None, transferer_second_leg_bridge: Bridge=None):
        """BridgeAttendedTransfer - a model defined in OpenAPI

        :param application: The application of this BridgeAttendedTransfer.
        :param timestamp: The timestamp of this BridgeAttendedTransfer.
        :param asterisk_id: The asterisk_id of this BridgeAttendedTransfer.
        :param type: The type of this BridgeAttendedTransfer.
        :param destination_application: The destination_application of this BridgeAttendedTransfer.
        :param destination_bridge: The destination_bridge of this BridgeAttendedTransfer.
        :param destination_link_first_leg: The destination_link_first_leg of this BridgeAttendedTransfer.
        :param destination_link_second_leg: The destination_link_second_leg of this BridgeAttendedTransfer.
        :param destination_threeway_bridge: The destination_threeway_bridge of this BridgeAttendedTransfer.
        :param destination_threeway_channel: The destination_threeway_channel of this BridgeAttendedTransfer.
        :param destination_type: The destination_type of this BridgeAttendedTransfer.
        :param is_external: The is_external of this BridgeAttendedTransfer.
        :param replace_channel: The replace_channel of this BridgeAttendedTransfer.
        :param result: The result of this BridgeAttendedTransfer.
        :param transfer_target: The transfer_target of this BridgeAttendedTransfer.
        :param transferee: The transferee of this BridgeAttendedTransfer.
        :param transferer_first_leg: The transferer_first_leg of this BridgeAttendedTransfer.
        :param transferer_first_leg_bridge: The transferer_first_leg_bridge of this BridgeAttendedTransfer.
        :param transferer_second_leg: The transferer_second_leg of this BridgeAttendedTransfer.
        :param transferer_second_leg_bridge: The transferer_second_leg_bridge of this BridgeAttendedTransfer.
        """
        self.openapi_types = {
            'application': str,
            'timestamp': date,
            'asterisk_id': str,
            'type': str,
            'destination_application': str,
            'destination_bridge': str,
            'destination_link_first_leg': Channel,
            'destination_link_second_leg': Channel,
            'destination_threeway_bridge': Bridge,
            'destination_threeway_channel': Channel,
            'destination_type': str,
            'is_external': bool,
            'replace_channel': Channel,
            'result': str,
            'transfer_target': Channel,
            'transferee': Channel,
            'transferer_first_leg': Channel,
            'transferer_first_leg_bridge': Bridge,
            'transferer_second_leg': Channel,
            'transferer_second_leg_bridge': Bridge
        }

        self.attribute_map = {
            'application': 'application',
            'timestamp': 'timestamp',
            'asterisk_id': 'asterisk_id',
            'type': 'type',
            'destination_application': 'destination_application',
            'destination_bridge': 'destination_bridge',
            'destination_link_first_leg': 'destination_link_first_leg',
            'destination_link_second_leg': 'destination_link_second_leg',
            'destination_threeway_bridge': 'destination_threeway_bridge',
            'destination_threeway_channel': 'destination_threeway_channel',
            'destination_type': 'destination_type',
            'is_external': 'is_external',
            'replace_channel': 'replace_channel',
            'result': 'result',
            'transfer_target': 'transfer_target',
            'transferee': 'transferee',
            'transferer_first_leg': 'transferer_first_leg',
            'transferer_first_leg_bridge': 'transferer_first_leg_bridge',
            'transferer_second_leg': 'transferer_second_leg',
            'transferer_second_leg_bridge': 'transferer_second_leg_bridge'
        }

        self._application = application
        self._timestamp = timestamp
        self._asterisk_id = asterisk_id
        self._type = type
        self._destination_application = destination_application
        self._destination_bridge = destination_bridge
        self._destination_link_first_leg = destination_link_first_leg
        self._destination_link_second_leg = destination_link_second_leg
        self._destination_threeway_bridge = destination_threeway_bridge
        self._destination_threeway_channel = destination_threeway_channel
        self._destination_type = destination_type
        self._is_external = is_external
        self._replace_channel = replace_channel
        self._result = result
        self._transfer_target = transfer_target
        self._transferee = transferee
        self._transferer_first_leg = transferer_first_leg
        self._transferer_first_leg_bridge = transferer_first_leg_bridge
        self._transferer_second_leg = transferer_second_leg
        self._transferer_second_leg_bridge = transferer_second_leg_bridge

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BridgeAttendedTransfer':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BridgeAttendedTransfer of this BridgeAttendedTransfer.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application(self):
        """Gets the application of this BridgeAttendedTransfer.

        Name of the application receiving the event.

        :return: The application of this BridgeAttendedTransfer.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this BridgeAttendedTransfer.

        Name of the application receiving the event.

        :param application: The application of this BridgeAttendedTransfer.
        :type application: str
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")

        self._application = application

    @property
    def timestamp(self):
        """Gets the timestamp of this BridgeAttendedTransfer.

        Time at which this event was created.

        :return: The timestamp of this BridgeAttendedTransfer.
        :rtype: date
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BridgeAttendedTransfer.

        Time at which this event was created.

        :param timestamp: The timestamp of this BridgeAttendedTransfer.
        :type timestamp: date
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def asterisk_id(self):
        """Gets the asterisk_id of this BridgeAttendedTransfer.

        The unique ID for the Asterisk instance that raised this event.

        :return: The asterisk_id of this BridgeAttendedTransfer.
        :rtype: str
        """
        return self._asterisk_id

    @asterisk_id.setter
    def asterisk_id(self, asterisk_id):
        """Sets the asterisk_id of this BridgeAttendedTransfer.

        The unique ID for the Asterisk instance that raised this event.

        :param asterisk_id: The asterisk_id of this BridgeAttendedTransfer.
        :type asterisk_id: str
        """

        self._asterisk_id = asterisk_id

    @property
    def type(self):
        """Gets the type of this BridgeAttendedTransfer.

        Indicates the type of this message.

        :return: The type of this BridgeAttendedTransfer.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BridgeAttendedTransfer.

        Indicates the type of this message.

        :param type: The type of this BridgeAttendedTransfer.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def destination_application(self):
        """Gets the destination_application of this BridgeAttendedTransfer.

        Application that has been transferred into

        :return: The destination_application of this BridgeAttendedTransfer.
        :rtype: str
        """
        return self._destination_application

    @destination_application.setter
    def destination_application(self, destination_application):
        """Sets the destination_application of this BridgeAttendedTransfer.

        Application that has been transferred into

        :param destination_application: The destination_application of this BridgeAttendedTransfer.
        :type destination_application: str
        """

        self._destination_application = destination_application

    @property
    def destination_bridge(self):
        """Gets the destination_bridge of this BridgeAttendedTransfer.

        Bridge that survived the merge result

        :return: The destination_bridge of this BridgeAttendedTransfer.
        :rtype: str
        """
        return self._destination_bridge

    @destination_bridge.setter
    def destination_bridge(self, destination_bridge):
        """Sets the destination_bridge of this BridgeAttendedTransfer.

        Bridge that survived the merge result

        :param destination_bridge: The destination_bridge of this BridgeAttendedTransfer.
        :type destination_bridge: str
        """

        self._destination_bridge = destination_bridge

    @property
    def destination_link_first_leg(self):
        """Gets the destination_link_first_leg of this BridgeAttendedTransfer.


        :return: The destination_link_first_leg of this BridgeAttendedTransfer.
        :rtype: Channel
        """
        return self._destination_link_first_leg

    @destination_link_first_leg.setter
    def destination_link_first_leg(self, destination_link_first_leg):
        """Sets the destination_link_first_leg of this BridgeAttendedTransfer.


        :param destination_link_first_leg: The destination_link_first_leg of this BridgeAttendedTransfer.
        :type destination_link_first_leg: Channel
        """

        self._destination_link_first_leg = destination_link_first_leg

    @property
    def destination_link_second_leg(self):
        """Gets the destination_link_second_leg of this BridgeAttendedTransfer.


        :return: The destination_link_second_leg of this BridgeAttendedTransfer.
        :rtype: Channel
        """
        return self._destination_link_second_leg

    @destination_link_second_leg.setter
    def destination_link_second_leg(self, destination_link_second_leg):
        """Sets the destination_link_second_leg of this BridgeAttendedTransfer.


        :param destination_link_second_leg: The destination_link_second_leg of this BridgeAttendedTransfer.
        :type destination_link_second_leg: Channel
        """

        self._destination_link_second_leg = destination_link_second_leg

    @property
    def destination_threeway_bridge(self):
        """Gets the destination_threeway_bridge of this BridgeAttendedTransfer.


        :return: The destination_threeway_bridge of this BridgeAttendedTransfer.
        :rtype: Bridge
        """
        return self._destination_threeway_bridge

    @destination_threeway_bridge.setter
    def destination_threeway_bridge(self, destination_threeway_bridge):
        """Sets the destination_threeway_bridge of this BridgeAttendedTransfer.


        :param destination_threeway_bridge: The destination_threeway_bridge of this BridgeAttendedTransfer.
        :type destination_threeway_bridge: Bridge
        """

        self._destination_threeway_bridge = destination_threeway_bridge

    @property
    def destination_threeway_channel(self):
        """Gets the destination_threeway_channel of this BridgeAttendedTransfer.


        :return: The destination_threeway_channel of this BridgeAttendedTransfer.
        :rtype: Channel
        """
        return self._destination_threeway_channel

    @destination_threeway_channel.setter
    def destination_threeway_channel(self, destination_threeway_channel):
        """Sets the destination_threeway_channel of this BridgeAttendedTransfer.


        :param destination_threeway_channel: The destination_threeway_channel of this BridgeAttendedTransfer.
        :type destination_threeway_channel: Channel
        """

        self._destination_threeway_channel = destination_threeway_channel

    @property
    def destination_type(self):
        """Gets the destination_type of this BridgeAttendedTransfer.

        How the transfer was accomplished

        :return: The destination_type of this BridgeAttendedTransfer.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this BridgeAttendedTransfer.

        How the transfer was accomplished

        :param destination_type: The destination_type of this BridgeAttendedTransfer.
        :type destination_type: str
        """
        if destination_type is None:
            raise ValueError("Invalid value for `destination_type`, must not be `None`")

        self._destination_type = destination_type

    @property
    def is_external(self):
        """Gets the is_external of this BridgeAttendedTransfer.

        Whether the transfer was externally initiated or not

        :return: The is_external of this BridgeAttendedTransfer.
        :rtype: bool
        """
        return self._is_external

    @is_external.setter
    def is_external(self, is_external):
        """Sets the is_external of this BridgeAttendedTransfer.

        Whether the transfer was externally initiated or not

        :param is_external: The is_external of this BridgeAttendedTransfer.
        :type is_external: bool
        """
        if is_external is None:
            raise ValueError("Invalid value for `is_external`, must not be `None`")

        self._is_external = is_external

    @property
    def replace_channel(self):
        """Gets the replace_channel of this BridgeAttendedTransfer.


        :return: The replace_channel of this BridgeAttendedTransfer.
        :rtype: Channel
        """
        return self._replace_channel

    @replace_channel.setter
    def replace_channel(self, replace_channel):
        """Sets the replace_channel of this BridgeAttendedTransfer.


        :param replace_channel: The replace_channel of this BridgeAttendedTransfer.
        :type replace_channel: Channel
        """

        self._replace_channel = replace_channel

    @property
    def result(self):
        """Gets the result of this BridgeAttendedTransfer.

        The result of the transfer attempt

        :return: The result of this BridgeAttendedTransfer.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this BridgeAttendedTransfer.

        The result of the transfer attempt

        :param result: The result of this BridgeAttendedTransfer.
        :type result: str
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")

        self._result = result

    @property
    def transfer_target(self):
        """Gets the transfer_target of this BridgeAttendedTransfer.


        :return: The transfer_target of this BridgeAttendedTransfer.
        :rtype: Channel
        """
        return self._transfer_target

    @transfer_target.setter
    def transfer_target(self, transfer_target):
        """Sets the transfer_target of this BridgeAttendedTransfer.


        :param transfer_target: The transfer_target of this BridgeAttendedTransfer.
        :type transfer_target: Channel
        """

        self._transfer_target = transfer_target

    @property
    def transferee(self):
        """Gets the transferee of this BridgeAttendedTransfer.


        :return: The transferee of this BridgeAttendedTransfer.
        :rtype: Channel
        """
        return self._transferee

    @transferee.setter
    def transferee(self, transferee):
        """Sets the transferee of this BridgeAttendedTransfer.


        :param transferee: The transferee of this BridgeAttendedTransfer.
        :type transferee: Channel
        """

        self._transferee = transferee

    @property
    def transferer_first_leg(self):
        """Gets the transferer_first_leg of this BridgeAttendedTransfer.


        :return: The transferer_first_leg of this BridgeAttendedTransfer.
        :rtype: Channel
        """
        return self._transferer_first_leg

    @transferer_first_leg.setter
    def transferer_first_leg(self, transferer_first_leg):
        """Sets the transferer_first_leg of this BridgeAttendedTransfer.


        :param transferer_first_leg: The transferer_first_leg of this BridgeAttendedTransfer.
        :type transferer_first_leg: Channel
        """
        if transferer_first_leg is None:
            raise ValueError("Invalid value for `transferer_first_leg`, must not be `None`")

        self._transferer_first_leg = transferer_first_leg

    @property
    def transferer_first_leg_bridge(self):
        """Gets the transferer_first_leg_bridge of this BridgeAttendedTransfer.


        :return: The transferer_first_leg_bridge of this BridgeAttendedTransfer.
        :rtype: Bridge
        """
        return self._transferer_first_leg_bridge

    @transferer_first_leg_bridge.setter
    def transferer_first_leg_bridge(self, transferer_first_leg_bridge):
        """Sets the transferer_first_leg_bridge of this BridgeAttendedTransfer.


        :param transferer_first_leg_bridge: The transferer_first_leg_bridge of this BridgeAttendedTransfer.
        :type transferer_first_leg_bridge: Bridge
        """

        self._transferer_first_leg_bridge = transferer_first_leg_bridge

    @property
    def transferer_second_leg(self):
        """Gets the transferer_second_leg of this BridgeAttendedTransfer.


        :return: The transferer_second_leg of this BridgeAttendedTransfer.
        :rtype: Channel
        """
        return self._transferer_second_leg

    @transferer_second_leg.setter
    def transferer_second_leg(self, transferer_second_leg):
        """Sets the transferer_second_leg of this BridgeAttendedTransfer.


        :param transferer_second_leg: The transferer_second_leg of this BridgeAttendedTransfer.
        :type transferer_second_leg: Channel
        """
        if transferer_second_leg is None:
            raise ValueError("Invalid value for `transferer_second_leg`, must not be `None`")

        self._transferer_second_leg = transferer_second_leg

    @property
    def transferer_second_leg_bridge(self):
        """Gets the transferer_second_leg_bridge of this BridgeAttendedTransfer.


        :return: The transferer_second_leg_bridge of this BridgeAttendedTransfer.
        :rtype: Bridge
        """
        return self._transferer_second_leg_bridge

    @transferer_second_leg_bridge.setter
    def transferer_second_leg_bridge(self, transferer_second_leg_bridge):
        """Sets the transferer_second_leg_bridge of this BridgeAttendedTransfer.


        :param transferer_second_leg_bridge: The transferer_second_leg_bridge of this BridgeAttendedTransfer.
        :type transferer_second_leg_bridge: Bridge
        """

        self._transferer_second_leg_bridge = transferer_second_leg_bridge
