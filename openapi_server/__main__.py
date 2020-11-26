import connexion
import os

from openapi_server.config.default import *

from openapi_server import encoder

port = int(os.environ.get('PORT', 8080))

def main():
    app = connexion.App(__name__, specification_dir='./openapi/')  
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml', arguments={'title': 'Historic Management API'})
    app.app.config.from_object(DevelopmentConfig)
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    app = main()
