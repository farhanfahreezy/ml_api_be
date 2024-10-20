from flask_restful import Api
from src.utils.errors import errors
from src.controllers.train import TrainController
from src.controllers.predict import PredictController
from src.controllers.status import StatusController
from src.controllers.user import UserController

routes = Api(
    catch_all_404s=True,
    errors=errors,
    prefix='/api'
)

routes.add_resource(TrainController, '/train')
routes.add_resource(PredictController, '/predict')
routes.add_resource(StatusController, '/status')
routes.add_resource(UserController, '/user')