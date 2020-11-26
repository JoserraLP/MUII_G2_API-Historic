import connexion
import six

import json

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

    success = util.append_to_json(visit.to_dict())

    if success:
        return "Successfully added data \n {}".format(visit.to_str())
    else:
        return "----- ERROR INSERTING NEW VISIT -----"

def get_all_historic():  # noqa: E501
    """Get all visits from historic

    Get all visits from historic # noqa: E501


    :rtype: str
    """
    
    visits = util.return_all_json_data()

    if visits:
        return visits
    else:
        return "----- FAILED FETCHING HISTORIC -----"


def get_visit(id):  # noqa: E501
    """Get one visit information

    Get one visit information # noqa: E501

    :param id: ID of visit to get information
    :type id: int

    :rtype: str
    """

    visit = util.return_json_data(id)

    if visit:
        return visit
    else:
        return "----- FAILED FETCHING VISIT WITH ID {} -----".format(id)
