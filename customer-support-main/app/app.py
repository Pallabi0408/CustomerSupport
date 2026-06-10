from flask import Flask, redirect, url_for
from app.config.config import Config
from app.database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    from app.routes.auth_routes import auth_bp
    from app.routes.dashboard_routes import dashboard_bp
    from app.routes.predict_routes import predict_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(predict_bp)
    
    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))
        
    return app
