# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.self_user_controller import api as self_user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Flask REST API for managing users',
          version='1.0',
          description='Flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(self_user_ns, path='/selfuser')
api.add_namespace(auth_ns)
