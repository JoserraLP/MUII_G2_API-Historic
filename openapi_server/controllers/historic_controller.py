import connexion
import six

from ..__main__ import db

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

    json_visit = {
        "person_mac": visit.person_mac,
        "date": visit.date,
        "time": visit.time
    }

    new_visit = Visit(person_mac=json_visit['person_mac'], date=json_visit['date'], time=json_visit['time'])
    db.session.add(new_visit)
    db.session.commit()


    return 'Nice POST'


def get_all_historic():  # noqa: E501
    """Get all visits from historic

    Get all visits from historic # noqa: E501


    :rtype: str
    """
    visits = Visit.query.all()
    results = [
        {
            "person_mac": visit.person_mac,
            "visit": visit.date,
            "date": visit.time
        } for visit in visits]

    return {"count": len(results), "visit": results}


def get_visit(id):  # noqa: E501
    """Get one visit&#39;s information

    Get one visit information # noqa: E501

    :param id: ID of visit to get information
    :type id: int

    :rtype: str
    """

    return 'do some magic!'
