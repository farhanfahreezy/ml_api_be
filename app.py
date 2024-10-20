import os
from flask import Flask
from src.config import config
from src.routes.routes import routes
from flask_swagger_ui import get_swaggerui_blueprint

# Flask App Initialization
app = Flask(__name__)
app.config.from_object(config.settings[os.environ.get('APPLICATION_ENV', 'default')])
app.register_blueprint(get_swaggerui_blueprint('/api/docs', '/static/api-docs.json',), url_prefix='/api/docs')


# Flask API Initialization
routes.init_app(app)