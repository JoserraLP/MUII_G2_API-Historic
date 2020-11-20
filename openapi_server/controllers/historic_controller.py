import connexion
import six

from openapi_server.models.visit import Visit  # noqa: E501
from openapi_server import util


def add_visit(visit):  # noqa: E501
    """Add a visit to historic

    Add a visit to historic # noqa: E501

    :param visit: 
    :type visit: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        visit = Visit.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_all_historic():  # noqa: E501
    """Get all visits from historic

    Get all visits from historic # noqa: E501


    :rtype: str
    """
    return 'do some magic!'


def get_visit(id):  # noqa: E501
    """Get one visit&#39;s information

    Get one visit information # noqa: E501

    :param id: ID of visit to get information
    :type id: int

    :rtype: str
    """
    return 'do some magic!'
