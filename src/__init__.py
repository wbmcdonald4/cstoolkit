from flask import Flask

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.app_context().push()

    from src.main.routes import main
    from src.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app