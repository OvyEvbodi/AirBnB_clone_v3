#!/usr/bin/python3
"""Runs up initialization routines for the ``views`` package"""

from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__, url_prefix = '/api/v1')
