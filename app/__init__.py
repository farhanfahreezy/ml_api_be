import os
from flask import Flask
from app.config import config
from app.routes.routes import routes

# Flask App Initialization
app = Flask(__name__)
app.config.from_object(config.settings[os.environ.get('APPLICATION_ENV', 'default')])

# Database ORM Initialization (TODO)
# skip

# Database Migration (TODO)
# skip

# Flask API Initialization
routes.init_app(app)