#!/usr/bin/python3
""" Flask Application """
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from
from models import storage
import os
import flasgger

template_folder = os.path.abspath(os.path.join(os.path.dirname(flasgger.__file__), 'ui3/templates'))
static_folder = os.path.abspath(os.path.join(os.path.dirname(flasgger.__file__), 'ui3/static'))


app = Flask(__name__, template_folder=template_folder, static_url_path='/flasgger_static', static_folder=static_folder)


app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


app.config['SWAGGER'] = {
    'title': 'Lexmax Restful API',
    'uiversion': 1
}

Swagger(app)


if __name__ == "__main__":
    """ Main Function """

    host = '0.0.0.0'
    port = '5000'
    app.run(host=host, port=port, threaded=True, debug=True)