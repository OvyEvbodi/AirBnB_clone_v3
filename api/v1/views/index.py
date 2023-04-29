from flask import jsonify, make_response
from api.v1.views import app_views

@app_views.route('/status')
def status():
    resp = make_response()
    return jsonify({'status': resp.status.split()[-1]})

