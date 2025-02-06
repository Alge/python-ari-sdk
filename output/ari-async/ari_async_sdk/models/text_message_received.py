# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from ari_async_sdk.models.base_model import Model
from ari_async_sdk.models.endpoint import Endpoint
from ari_async_sdk.models.event import Event
from ari_async_sdk.models.text_message import TextMessage
from ari_async_sdk import util


class TextMessageReceived(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, application: str=None, timestamp: date=None, asterisk_id: str=None, type: str=None, endpoint: Endpoint=None, message: TextMessage=None):
        """TextMessageReceived - a model defined in OpenAPI

        :param application: The application of this TextMessageReceived.
        :param timestamp: The timestamp of this TextMessageReceived.
        :param asterisk_id: The asterisk_id of this TextMessageReceived.
        :param type: The type of this TextMessageReceived.
        :param endpoint: The endpoint of this TextMessageReceived.
        :param message: The message of this TextMessageReceived.
        """
        self.openapi_types = {
            'application': str,
            'timestamp': date,
            'asterisk_id': str,
            'type': str,
            'endpoint': Endpoint,
            'message': TextMessage
        }

        self.attribute_map = {
            'application': 'application',
            'timestamp': 'timestamp',
            'asterisk_id': 'asterisk_id',
            'type': 'type',
            'endpoint': 'endpoint',
            'message': 'message'
        }

        self._application = application
        self._timestamp = timestamp
        self._asterisk_id = asterisk_id
        self._type = type
        self._endpoint = endpoint
        self._message = message

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TextMessageReceived':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TextMessageReceived of this TextMessageReceived.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application(self):
        """Gets the application of this TextMessageReceived.

        Name of the application receiving the event.

        :return: The application of this TextMessageReceived.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this TextMessageReceived.

        Name of the application receiving the event.

        :param application: The application of this TextMessageReceived.
        :type application: str
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")

        self._application = application

    @property
    def timestamp(self):
        """Gets the timestamp of this TextMessageReceived.

        Time at which this event was created.

        :return: The timestamp of this TextMessageReceived.
        :rtype: date
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TextMessageReceived.

        Time at which this event was created.

        :param timestamp: The timestamp of this TextMessageReceived.
        :type timestamp: date
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def asterisk_id(self):
        """Gets the asterisk_id of this TextMessageReceived.

        The unique ID for the Asterisk instance that raised this event.

        :return: The asterisk_id of this TextMessageReceived.
        :rtype: str
        """
        return self._asterisk_id

    @asterisk_id.setter
    def asterisk_id(self, asterisk_id):
        """Sets the asterisk_id of this TextMessageReceived.

        The unique ID for the Asterisk instance that raised this event.

        :param asterisk_id: The asterisk_id of this TextMessageReceived.
        :type asterisk_id: str
        """

        self._asterisk_id = asterisk_id

    @property
    def type(self):
        """Gets the type of this TextMessageReceived.

        Indicates the type of this message.

        :return: The type of this TextMessageReceived.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TextMessageReceived.

        Indicates the type of this message.

        :param type: The type of this TextMessageReceived.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def endpoint(self):
        """Gets the endpoint of this TextMessageReceived.


        :return: The endpoint of this TextMessageReceived.
        :rtype: Endpoint
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this TextMessageReceived.


        :param endpoint: The endpoint of this TextMessageReceived.
        :type endpoint: Endpoint
        """

        self._endpoint = endpoint

    @property
    def message(self):
        """Gets the message of this TextMessageReceived.


        :return: The message of this TextMessageReceived.
        :rtype: TextMessage
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TextMessageReceived.


        :param message: The message of this TextMessageReceived.
        :type message: TextMessage
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message
