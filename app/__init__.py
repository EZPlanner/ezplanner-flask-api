from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    from app.server import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from app.Model import db
    db.init_app(app)

    return app

app = create_app('config');