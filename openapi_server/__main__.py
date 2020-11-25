#!/usr/bin/env python3

import connexion
import os

from flask_sqlalchemy import SQLAlchemy

from openapi_server import encoder

db = SQLAlchemy()

def main():

    port = int(os.environ.get('PORT', 5000))
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml', arguments={'title': 'Historic Management API'})
    app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://eajqjsmpybzzsb:57299d6e97a50490ba632dcb9349ab709596083ea5854f82d44004712bec49c6@ec2-54-217-236-206.eu-west-1.compute.amazonaws.com:5432/d8ca6n547ht0fo'
    db.init_app(app.app)

    # Create the tables with the application context
    with app.app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
