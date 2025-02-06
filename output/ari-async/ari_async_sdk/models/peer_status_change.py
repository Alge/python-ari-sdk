# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from ari_async_sdk.models.base_model import Model
from ari_async_sdk.models.endpoint import Endpoint
from ari_async_sdk.models.event import Event
from ari_async_sdk.models.peer import Peer
from ari_async_sdk import util


class PeerStatusChange(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, application: str=None, timestamp: date=None, asterisk_id: str=None, type: str=None, endpoint: Endpoint=None, peer: Peer=None):
        """PeerStatusChange - a model defined in OpenAPI

        :param application: The application of this PeerStatusChange.
        :param timestamp: The timestamp of this PeerStatusChange.
        :param asterisk_id: The asterisk_id of this PeerStatusChange.
        :param type: The type of this PeerStatusChange.
        :param endpoint: The endpoint of this PeerStatusChange.
        :param peer: The peer of this PeerStatusChange.
        """
        self.openapi_types = {
            'application': str,
            'timestamp': date,
            'asterisk_id': str,
            'type': str,
            'endpoint': Endpoint,
            'peer': Peer
        }

        self.attribute_map = {
            'application': 'application',
            'timestamp': 'timestamp',
            'asterisk_id': 'asterisk_id',
            'type': 'type',
            'endpoint': 'endpoint',
            'peer': 'peer'
        }

        self._application = application
        self._timestamp = timestamp
        self._asterisk_id = asterisk_id
        self._type = type
        self._endpoint = endpoint
        self._peer = peer

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PeerStatusChange':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PeerStatusChange of this PeerStatusChange.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application(self):
        """Gets the application of this PeerStatusChange.

        Name of the application receiving the event.

        :return: The application of this PeerStatusChange.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this PeerStatusChange.

        Name of the application receiving the event.

        :param application: The application of this PeerStatusChange.
        :type application: str
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")

        self._application = application

    @property
    def timestamp(self):
        """Gets the timestamp of this PeerStatusChange.

        Time at which this event was created.

        :return: The timestamp of this PeerStatusChange.
        :rtype: date
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PeerStatusChange.

        Time at which this event was created.

        :param timestamp: The timestamp of this PeerStatusChange.
        :type timestamp: date
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def asterisk_id(self):
        """Gets the asterisk_id of this PeerStatusChange.

        The unique ID for the Asterisk instance that raised this event.

        :return: The asterisk_id of this PeerStatusChange.
        :rtype: str
        """
        return self._asterisk_id

    @asterisk_id.setter
    def asterisk_id(self, asterisk_id):
        """Sets the asterisk_id of this PeerStatusChange.

        The unique ID for the Asterisk instance that raised this event.

        :param asterisk_id: The asterisk_id of this PeerStatusChange.
        :type asterisk_id: str
        """

        self._asterisk_id = asterisk_id

    @property
    def type(self):
        """Gets the type of this PeerStatusChange.

        Indicates the type of this message.

        :return: The type of this PeerStatusChange.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PeerStatusChange.

        Indicates the type of this message.

        :param type: The type of this PeerStatusChange.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def endpoint(self):
        """Gets the endpoint of this PeerStatusChange.


        :return: The endpoint of this PeerStatusChange.
        :rtype: Endpoint
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this PeerStatusChange.


        :param endpoint: The endpoint of this PeerStatusChange.
        :type endpoint: Endpoint
        """
        if endpoint is None:
            raise ValueError("Invalid value for `endpoint`, must not be `None`")

        self._endpoint = endpoint

    @property
    def peer(self):
        """Gets the peer of this PeerStatusChange.


        :return: The peer of this PeerStatusChange.
        :rtype: Peer
        """
        return self._peer

    @peer.setter
    def peer(self, peer):
        """Sets the peer of this PeerStatusChange.


        :param peer: The peer of this PeerStatusChange.
        :type peer: Peer
        """
        if peer is None:
            raise ValueError("Invalid value for `peer`, must not be `None`")

        self._peer = peer
