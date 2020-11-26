import connexion
import os

from openapi_server.config.default import *

from openapi_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/') 
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml', arguments={'title': 'Historic Management API'})
    app.app.config.from_object(DevelopmentConfig)
    app.run()

app = main()

if __name__ == '__main__':
    app = main()
