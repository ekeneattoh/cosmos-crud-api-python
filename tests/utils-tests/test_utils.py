import unittest
from Shared.utils import *
import json


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.data = {
            "firstname": "Ekene",
            "lastname": "Attoh",
            "_id": "ekeneattoh@test.com",
            "company_name": "cocuisson"
        }
        self.db_name = "cocuisson-dev"
        self.collection_name = "users"

    def tearDown(self) -> None:
        delete_one_in_collection(db_name=self.db_name, collection_name=self.collection_name,
                                 search_query={"_id": "ekeneattoh@test.com"})

    def test_insert_one_into_db_collection(self):
        """

        :return:
        """
        insert_test = insert_one_into_db_collection(db_name=self.db_name, collection_name=self.collection_name,
                                                    data=self.data)

        assert insert_test["data"] == "OK"

    def test_find_one_in_collection(self):
        """

        :return:
        """

        # add the data first
        insert_one_into_db_collection(db_name=self.db_name, collection_name=self.collection_name,
                                      data=self.data)

        find_result = find_one_in_collection(db_name=self.db_name, collection_name=self.collection_name,
                                             search_query={"_id": "ekeneattoh@test.com"})

        assert find_result["status_message"] == "OK"

    def test_find_many_in_collection(self):
        """

        :return:
        """

        # add the data first
        insert_one_into_db_collection(db_name=self.db_name, collection_name=self.collection_name,
                                      data=self.data)

        data_two = {
            "firstname": "Manon",
            "lastname": "Picot",
            "_id": "manonpicot@test.com",
            "company_name": "cocuisson"
        }

        insert_one_into_db_collection(db_name=self.db_name, collection_name=self.collection_name,
                                      data=data_two)

        find_result = find_many_in_collection(db_name=self.db_name, collection_name=self.collection_name,
                                              search_query={"company_name": "cocuisson"})

        assert len(find_result["data"]) == 2

        delete_one_in_collection(db_name=self.db_name, collection_name=self.collection_name,
                                 search_query={"_id": "manonpicot@test.com"})

    def test_update_one_into_db_collection(self):
        """

        :return:
        """
        insert_one_into_db_collection(db_name=self.db_name, collection_name=self.collection_name,
                                      data=self.data)

        update_result = update_one_set_in_collection(db_name=self.db_name, collection_name=self.collection_name,
                                                     search_query={"_id": "ekeneattoh@test.com"},
                                                     update_query={"company_name": "Onaide"})

        assert update_result["data"] == "OK"
