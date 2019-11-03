"""this is init or src"""

from flask import Flask
from .util import school_blueprint


def create_app():
    """
    Create application
    """
    app = Flask(__name__)
    app.register_blueprint(school_blueprint)

    @app.route('/actuator/health', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Welcome to Python Flask API'
    return app

