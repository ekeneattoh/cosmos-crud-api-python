import unittest
from Shared.utils import *
import json


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.data = {
            "firstname": "Ekene",
            "lastname": "Attoh",
            "_id": "ekeneattoh@test.com"
        }

    def test_insert_one_into_db_collection(self):
        """

        :return:
        """
        insert_test = insert_one_into_db_collection(db_name="cocuisson-dev", collection_name="users", data=self.data)

        assert insert_test["data"] == "OK"

