"""Renders api data using Flask"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv


def create_app():
    app = Flask(__name__)

    app.register_blueprint(app_views)
    return app

    @app.teardown_appcontext
    def shutdown(self):
        """Tear down function for app context"""

        storage.close()


if __name__ == '__main__':
    app = create_app()
    port_env = getenv('HBNB_API_PORT', '5000')
    host_env = getenv('HBNB_API_HOST', '0.0.0.0')
    app.config['PRETTYPRINT'] = True

    app.run(host=host_env, port=port_env, threaded=True)