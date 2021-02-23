import os
import json
import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    secret_key = os.environ.get("SECRET_KEY")

    if secret_key is not None:
        return func.HttpResponse(
            body=json.dumps({"value": secret_key}),
            status_code=200,
            mimetype="application/json"
        )
    else:
        msg = "secret_key environment variable not found"
        logging.error(msg)
        return func.HttpResponse(
            body=json.dumps({"error": msg}),
            status_code=404,
            mimetype="application/json"
        )