from flask_restful import Api
from app.utils.errors import errors
from app.controllers.train import Train
from app.controllers.predict import Predict
from app.controllers.status import Status

routes = Api(
    catch_all_404s=True,
    errors=errors,
    prefix='/api'
)

routes.add_resource(Train, '/train')
routes.add_resource(Predict, '/predict')
routes.add_resource(Status, '/status')