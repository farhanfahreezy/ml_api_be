from flask import request
from flask_restful import Resource
from bcrypt import checkpw, gensalt , hashpw
from flask_jwt_extended import create_access_token
from datetime import timedelta
from src.models import User
from src.utils.db import db


class SignInController(Resource):
    def post(self):
        try:
            # Get request body
            body = request.get_json()
            username = body.get('username')
            password = body.get('password')

            if not username or not password:
                return {"message": "Missing username or password"}, 400
            
            user = User.query.filter_by(username=username).first()

            if not user:
                return {'message': 'Username not found'}, 404
            
            if not checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return {'message': 'Incorrect credentials'}, 401 
            
            access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=10))
            return {"access_token":access_token}, 200
        
        except Exception as e:
             return {"message": f"An error occurred: {str(e)}"}, 500

class SignUpController(Resource):
    def post(self):
        try:
            # Get request body
            body = request.get_json()
            name = body.get('name')
            username = body.get('username')
            password = body.get('password')
            email = body.get('email')

            if (not (email and name and username and password)):
                return {'message': 'Name, username, email and password are required'}, 400
            
            salt = gensalt()
            hashed_password = hashpw(password.encode('utf-8'), salt)

            new_user = User(
                name=name,
                username=username,
                password=hashed_password.decode('utf-8'),
                email=email
            )
        
            db.session.add(new_user)
            db.session.commit()
            return {'message': 'User created successfully'}, 201
        
        except Exception as e:
            db.session.rollback()
            return {'message': f'Error occurred: {str(e)}'}, 500

            

        