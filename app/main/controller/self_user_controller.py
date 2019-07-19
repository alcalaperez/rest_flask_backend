from flask import request
from flask_restplus import Resource, Api

from ..util.SelfUserDTO import SelfUserDto
from app.main.util.login_filter import token_required
from app.main.service.auth_helper import Auth

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}
api = SelfUserDto.api
api.authorizations = authorizations
_user = SelfUserDto.selfuser


@api.route('/')
class UserList(Resource):
    @token_required
    @api.doc('Who I am')
    @api.doc(security='apikey')
    def get(self):
        """Information about the logged user (JWT info)"""
        data, status = Auth.get_logged_in_user(request)
        return data.get('data')
