from functools import wraps
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from jwt import decode
from flask import request, current_app

def jwt_auth(fn):
    @wraps(fn)
    def decorated(*args, **kwargs):
        try:
            # Retrieve the JWT from the Authorization header
            auth_header = request.headers.get('Authorization', None)
            if not auth_header:
                return {"message": "Missing authorization header."}, 401 

            # extract token
            token = auth_header.split(" ")[1] if " " in auth_header else auth_header

            jwt_secret = current_app.config['JWT_SECRET_KEY']
            decoded_jwt = decode(token, jwt_secret, algorithms=["HS256"])

            print("Decoded JWT:", decoded_jwt) 

            # forward
            return fn(*args, **kwargs)

        except ExpiredSignatureError:
            return {"message": "Token has expired."}, 401
        except InvalidTokenError:
            return {"message": "Invalid token."}, 401
        except Exception as e:
            return {"message": str(e)}, 500
    return decorated