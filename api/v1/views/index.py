#!/usr/bin/python3
"""Handles the logic for the index of the api for the AirBnB clone project"""

from api.v1.views import app_views
from flask import make_response, jsonify


@app_views.route('/status')
def api_status():
    """Route for api status"""
    response = make_response().status.split()[-1]
    return make_response(jsonify({"status": response}))
