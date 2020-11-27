import connexion
import six

import json

from openapi_server.models.visit import Visit  # noqa: E501
from openapi_server import util

import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

def add_visit(visit):  # noqa: E501
    """Add a visit to historic

    Add a visit to historic # noqa: E501

    :param visit: 
    :type visit: dict | bytes

    :rtype: str
    """

    if connexion.request.is_json:
        visit = Visit.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        conn = psycopg2.connect(host=DATABASE_URL, sslmode='require')

        cursor = conn.cursor()

        query = """ INSERT INTO historic (person_mac, date, time) VALUES (%s,%s,%s)"""
        visit_data = (visit.person_mac, visit.date, visit.time)
        cursor.execute(query, visit_data)

        conn.commit()
        count = cursor.rowcount
        return "Record inserted successfully into historic table"

    except (Exception, psycopg2.Error) as error :
        if(conn):
            return "Failed to insert record into historic table. Error =>  {}".format(error)
    
    finally:
        #closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

def get_all_historic():  # noqa: E501
    """Get all visits from historic

    Get all visits from historic # noqa: E501


    :rtype: str
    """
    
    try:
        conn = psycopg2.connect(host=DATABASE_URL, sslmode='require')

        cursor = conn.cursor()
        query = "SELECT * FROM historic"

        cursor.execute(query)
        print("Selecting rows from historic table using cursor.fetchall")
        historic_records = cursor.fetchall() 
        
        print("Print each row and it's columns values")
        for row in historic_records:
            print("id = ", row[0], )
            print("person_mac = ", row[1], )
            print("date = ", row[2])
            print("time  = ", row[3], "\n")

        return historic_records

    except (Exception, psycopg2.Error) as error :
        return "Error while fetching data from PostgreSQL. Error => {}".format(error)

    finally:
        #closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")


def get_visit(id):  # noqa: E501
    """Get one visit information

    Get one visit information # noqa: E501

    :param id: ID of visit to get information
    :type id: int

    :rtype: str
    """

    try:
        conn = psycopg2.connect(host=DATABASE_URL, sslmode='require')

        cursor = conn.cursor()
        query = "SELECT * FROM historic WHERE id = {}".format(id)

        cursor.execute(query)
        print("Selecting rows from historic table using cursor.fetchall")
        historic_records = cursor.fetchall() 
        
        print("Print each row and it's columns values")
        for row in historic_records:
            print("id = ", row[0], )
            print("person_mac = ", row[1], )
            print("date = ", row[2])
            print("time  = ", row[3], "\n")

        return historic_records

    except (Exception, psycopg2.Error) as error :
        return "Error while fetching data from PostgreSQL. Error => {}".format(error)

    finally:
        #closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
