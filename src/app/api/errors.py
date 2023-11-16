from src.app.exceptions import ValidationError
from src.app.api.rest_api import api
from flask import current_app
from http import HTTPStatus


@api.errorhandler(ValidationError)
def validation_error(e):
    current_app.logger.error(e)
    return {'error_cause':e.args[0]},HTTPStatus.BAD_REQUEST