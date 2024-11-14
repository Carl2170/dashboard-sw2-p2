from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from .routes import main_routes  # Asegúrate de importar el Blueprint correctamente

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar Blueprints (rutas)
    app.register_blueprint(main_routes)  # Registra el blueprint con las rutas

    
    return app
