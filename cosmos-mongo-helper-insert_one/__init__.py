import logging

import azure.functions as func

from Shared.utils import insert_one_into_db_collection

import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()

        if "db_name" in req_body.keys() and "collection_name" in req_body.keys():

            db_name = req_body["db_name"]
            collection_name = req_body["collection_name"]

            req_body.pop("db_name")
            req_body.pop("collection_name")

            insert_one_result = insert_one_into_db_collection(db_name=db_name, collection_name=collection_name,
                                                              data=req_body)

            if insert_one_result["status_message"] == "OK":
                return func.HttpResponse(json.dumps(insert_one_result), status_code=200)
            elif insert_one_result["status_message"] == "ERROR":
                return func.HttpResponse(json.dumps(insert_one_result), status_code=400)
        else:
            return func.HttpResponse(
                "Please pass valid JSON in the request body.",
                status_code=400
            )
    except ValueError:
        return func.HttpResponse(
            "Please pass valid JSON in the request body.",
            status_code=400
        )
