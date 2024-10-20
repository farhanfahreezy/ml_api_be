from flask_restful import Api
from src.utils.errors import errors
from src.controllers.train import Train
from src.controllers.predict import Predict
from src.controllers.status import Status

routes = Api(
    catch_all_404s=True,
    errors=errors,
    prefix='/api'
)

routes.add_resource(Train, '/train')
routes.add_resource(Predict, '/predict')
routes.add_resource(Status, '/status')