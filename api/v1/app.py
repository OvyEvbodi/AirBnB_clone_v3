"""Renders api data using Flask"""
from flask import Flask
from models import storage
from os import getenv


def create_app():
    app = Flask(__name__)

    app.register_blueprint('app_views')

    @app.teardown_appcontext
    def shutdown(self):
        """Tear down function for app context"""

        storage.close()


if __name__ == '__main__':
    create_app()
    port_env = getenv(HBNB_API_PORT)
    host_env = getenv(HBNB_API_HOST)


    if not host_env:
        host_env = '0.0.0.0'
    if not port_env:
        port_env = '5000'

    app.run(host=host_env, port=port_env, threaded=True)