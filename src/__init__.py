from flask import Flask
from src.config import Config



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.app_context().push()

    from src.main.routes import main
    # from src.errors.handlers import errors
    app.register_blueprint(main)
    # app.register_blueprint(errors)

    return app