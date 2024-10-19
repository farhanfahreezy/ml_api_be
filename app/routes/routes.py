from flask_restful import Api
from app.utils.errors import errors
from app.controllers.test import Test

routes = Api(
    catch_all_404s=True,
    errors=errors,
    prefix='/api'
)

routes.add_resource(Test, '/test')