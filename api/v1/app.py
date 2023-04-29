from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

HOST = getenv('HBNB_API_HOST', '0.0.0.0')
PORT = getenv('HBNB_API_PORT', 5000)

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')

@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, threaded=True)

