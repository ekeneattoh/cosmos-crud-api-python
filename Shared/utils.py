import pymongo
from pymongo.errors import WriteError, PyMongoError

client = pymongo.MongoClient(
    "mongodb+srv://onaide-dev:Aderonke!4@cluster0.v3ppc.mongodb.net/cocuisson-dev?retryWrites=true&w=majority")


def get_database(db_name: str):
    return client[db_name]


def insert_one_into_db_collection(db_name: str, collection_name: str, data: dict) -> dict:
    """

    :param db_name: name of the db
    :param collection_name: name of the db collection
    :param data: data to be inserted
    :return: dict of the result of the insert
    """

    result = {}

    db = get_database(db_name=db_name)

    collection = db[collection_name]

    try:
        insert_result = collection.insert_one(data)
        if insert_result.inserted_id is not None:
            result["data"] = "OK"
            result["status_message"] = "OK"

    except WriteError as e:
        result["data"] = str(e)
        result["status_message"] = "ERROR"

    return result


def find_one_in_collection(db_name: str, collection_name: str, search_query: dict) -> dict:
    """

    :param db_name: name of the db
    :param collection_name: name of the db collection
    :param search_query: search query
    :return: dictionary of document found
    """

    result = {}

    db = get_database(db_name=db_name)

    collection = db[collection_name]

    try:
        result_document = collection.find_one(filter=search_query)
        if result_document is not None:
            result["data"] = result_document
            result["status_message"] = "OK"
        else:
            result["data"] = "Document does not exist!"
            result["status_message"] = "ERROR"
    except PyMongoError as e:
        result["data"] = str(e)
        result["status_message"] = "ERROR"

    return result


def find_many_in_collection(db_name: str, collection_name: str, search_query: dict) -> dict:
    """

    :param db_name: name of the db
    :param collection_name: name of the db collection
    :param search_query: search query
    :return: dictionary of documents found
    """

    result = {}
    result_document_list = []

    db = get_database(db_name=db_name)

    collection = db[collection_name]

    try:
        result_documents = collection.find(filter=search_query)

        for document in result_documents:
            result_document_list.append(document)

        if len(result_document_list) != 0:
            result["data"] = result_document_list
            result["status_message"] = "OK"
        else:
            result["data"] = "No documents found matching that query"
            result["status_message"] = "ERROR"
    except PyMongoError as e:
        result["data"] = str(e)
        result["status_message"] = "ERROR"

    return result


def update_one_set_in_collection(db_name: str, collection_name: str, search_query: dict, update_query: dict) -> dict:
    """

    :param db_name: name of the db
    :param collection_name: name of the db collection
    :param search_query: search query
    :param update_query: modification dict
    :return: dictionary of document found
    """

    result = {}

    db = get_database(db_name=db_name)

    collection = db[collection_name]

    try:
        result_document = collection.update_one(filter=search_query, update={"$set": update_query})
        if result_document.modified_count == 1:
            result["data"] = "OK"
            result["status_message"] = "OK"
        if result_document.matched_count != 1:
            result["data"] = "No documents found matching that query"
            result["status_message"] = "ERROR"

    except WriteError as e:
        result["data"] = str(e)
        result["status_message"] = "ERROR"

    return result


def delete_one_in_collection(db_name: str, collection_name: str, search_query: dict) -> dict:
    """

    :param db_name: name of the db
    :param collection_name: name of the db collection
    :param search_query: search query
    :return: dictionary of document found
    """

    result = {}

    db = get_database(db_name=db_name)

    collection = db[collection_name]

    try:
        result_document = collection.delete_one(filter=search_query)
        if result_document is not None:
            result["data"] = result_document
            result["status_message"] = "OK"
        else:
            result["data"] = "Document does not exist!"
            result["status_message"] = "ERROR"
    except PyMongoError as e:
        result["data"] = str(e)
        result["status_message"] = "ERROR"

    return result
