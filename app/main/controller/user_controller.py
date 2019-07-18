from flask import request
from flask_restplus import Resource

from ..util.UserDTO import UserDto
from ..service.user_service import save_new_user, get_all_users, get_user_by_id, get_user_by_email

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()


@api.response(201, 'User successfully created.')
@api.doc('create a new user')
@api.expect(_user, validate=True)
def post(self):
    """Creates a new User """
    data = request.json
    return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('Find an user by id')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_user_by_id(public_id)
        if not user:
            api.abort(404)
        else:
            return user


@api.route('/<email>')
@api.param('email', 'The email of the user')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('Find an user by email')
    @api.marshal_with(_user)
    def get(self, email):
        """get a user given its email"""
        user = get_user_by_email(email)
        if not user:
            api.abort(404)
        else:
            return user