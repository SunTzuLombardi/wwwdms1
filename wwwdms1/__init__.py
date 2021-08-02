from flask import Flask
from wwwdms1.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
  
    from wwwdms1.main.routes import main
    from wwwdms1.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
