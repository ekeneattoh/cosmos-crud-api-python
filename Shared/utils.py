import pymongo
from pymongo.errors import WriteError

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

    db = get_database(db_name=db_name)

    collection = db[collection_name]

    try:
        insert_result = collection.insert_one(data)

    except WriteError as e:
        raise Exception(e)

    if insert_result.inserted_id is not None:
        return {
            "data": "OK"
        }
