import connexion
from flask import jsonify
from muii_g2_family_lock_database.Database import PostgresDB

from openapi_server.models.visit import Visit  # noqa: E501


def add_visit(visit):  # noqa: E501
    """Add a visit to historic

    Add a visit to historic # noqa: E501

    :param visit: 
    :type visit: dict | bytes

    :rtype: str
    """

    if connexion.request.is_json:
        visit = Visit.from_dict(connexion.request.get_json())  # noqa: E501

    db = PostgresDB()
    error = db.add_visit(visit.person_mac, visit.date, visit.time)
    if error:
        return error
    return "Record inserted successfully into historic table"


def get_all_historic():  # noqa: E501
    """Get all visits from historic

    Get all visits from historic # noqa: E501


    :rtype: str
    """
    db = PostgresDB()
    historic_records = db.get_all_historic()
    if "Error" in historic_records:
        return historic_records

    data = {"historic": []}

    for row in historic_records:
        data['historic'].append(
            {
                "id": row[0],
                "person_MAC": row[1],
                "date": row[2],
                "hour": row[3]
            }
        )
    return jsonify(data)


def get_visit(id):  # noqa: E501
    """Get one visit information

    Get one visit information # noqa: E501

    :param id: ID of visit to get information
    :type id: int

    :rtype: str
    """
    db = PostgresDB()
    visit = db.get_visit(id)
    if "Error" in visit:
        return visit
    data = {"visit": []}
    for row in visit:
        data['visit'].append(
            {
                "id": row[0],
                "person_MAC": row[1],
                "date": row[2],
                "hour": row[3]
            }
        )

    return jsonify(data)
