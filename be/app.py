from flask import Flask, request, jsonify
from flask_cors import CORS
from database import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)
    CORS(app)

    from routes import main
    app.register_blueprint(main)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(port=8080, debug=True)
