import logging

import azure.functions as func

from Shared.utils import delete_one_in_collection

import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()

        if "db_name" in req_body.keys() and "collection_name" in req_body.keys():

            db_name = req_body["db_name"]
            collection_name = req_body["collection_name"]

            search_query_doc = req_body["data"]

            delete_one_result = delete_one_in_collection(db_name=db_name, collection_name=collection_name,
                                                         search_query=search_query_doc)

            if delete_one_result["status_message"] == "OK":
                return func.HttpResponse(json.dumps(delete_one_result), status_code=200)
            elif delete_one_result["status_message"] == "ERROR" and delete_one_result[
                "data"] == "Document does not exist!":
                return func.HttpResponse(json.dumps(delete_one_result), status_code=404)
        else:
            return func.HttpResponse(
                "Please pass valid JSON in the request body.",
                status_code=400
            )
    except ValueError as e:
        return func.HttpResponse(
            str(e),
            status_code=400
        )
