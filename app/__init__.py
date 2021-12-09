#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: BENULL
@time: 2021/12/8 下午8:54
"""
from flask import Flask as _Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask.json import JSONEncoder as _JSONEncoder

db = SQLAlchemy()


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)


class Flask(_Flask):
    json_encoder = JSONEncoder


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
