#!/usr/bin/env python3

import connexion
import os

from .app import create_app

from openapi_server.config.default import *

from openapi_server import encoder

port = int(os.environ.get('PORT', 8080))

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=port)