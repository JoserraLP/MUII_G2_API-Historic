#!/usr/bin/env python3

import connexion
import os

from openapi_server.config.default import *

from openapi_server import encoder

app = connexion.App(__name__, specification_dir='./openapi/')  

def create_app():
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml', arguments={'title': 'Historic Management API'})
    app.app.config.from_object(DevelopmentConfig)

    return app