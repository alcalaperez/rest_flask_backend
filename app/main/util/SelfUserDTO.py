from flask_restplus import Namespace, fields


class SelfUserDto:
    api = Namespace('self user', description='self user related operations')
    selfuser = api.model('self_user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'admin': fields.String(required=True, description='user admin'),
        'public_id': fields.String(description='user Identifier')
    })
