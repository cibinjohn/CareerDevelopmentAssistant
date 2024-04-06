from pymongo import MongoClient

from log.cj_logger import cj_logger


class MongoDBHandler:
    def __init__(self, host='localhost', port=27017, db_name='test'):
        port = int(port)
        self.client = MongoClient(host, port)
        print("Connected to MongoDB")
        self.databases_list = self.list_databases()
        if db_name not in self.databases_list:
            print("db : {} do not exist, creating one...".format(db_name))
        self.db = self.client[db_name]
        print("connected to the database {}".format(self.db))

    def list_collections(self):
        return self.db.list_collection_names()

    def get_all_data(self, collection_name):
        collection = self.db[collection_name]
        return list(collection.find())

    def add_data(self, collection_name, data):
        collection = self.db[collection_name]
        return collection.insert_one(data)

    def update_data(self, collection_name, query, new_data):
        collection = self.db[collection_name]
        return collection.update_one(query, {'$set': new_data})

    def modify_data(self, collection_name, query, updated_fields):
        collection = self.db[collection_name]
        return collection.update_one(query, {'$set': updated_fields})

    def delete_collection(self, collection_name):
        collection = self.db[collection_name]
        return collection.drop()

    def list_databases(self):
        return self.client.list_database_names()

    def create_collection(self, collection_name):
        if collection_name not in self.list_collections():
            self.db.create_collection(collection_name)
            return f"Collection '{collection_name}' created successfully."
        else:
            return f"Collection '{collection_name}' already exists."

    def get_documents_by_key_value(self, collection_name, conditions):
        cj_logger.info("---get_documents_by_key_value start---")
        collection = self.db[collection_name]
        values = collection.find(conditions)
        cj_logger.info("values : ".format(values))
        has_email = any(item.get("email") for item in values)
        if has_email:
            return list(collection.find(conditions))
        else:
            cj_logger.info("Credentials not valid")
            cj_logger.info("conditions : {}".format(conditions))
            cj_logger.info("Available credentials : {}".format(self.get_all_data(collection_name)))
            return None


class UserCredentialsHandler(MongoDBHandler):
    def __init__(self, host='localhost', port=27017, db_name='test', collection_name='credentials'):
        super().__init__(host, port, db_name)

        self.collection = collection_name

        if self.collection not in self.list_collections():
            print("Collection {} does not exist, Creating it...".format(self.collection))
            self.create_collection(self.collection)

    def create_user(self, email, password):
        # Check if the email already exists
        docs = self.get_documents_by_key_value(collection_name=self.collection,
                                           conditions={"email":email})
        if docs:
            return "failure", "Email already exists. Please use a different email."

        # If email does not exist, create a new document for the user
        user_data = {"email": email, "password": password}
        self.add_data(self.collection, user_data)
        return "success","User credentials created successfully."

    def check_credentials(self, email, password):
        # Check if the provided email and password combination exists
        filter = {"email": email, "password": password}
        cj_logger.info("filter : {}".format(filter))
        docs = self.get_documents_by_key_value(collection_name=self.collection,
                                               conditions=filter)
        # print(docs)
        # user = self.collection.find_one({"email": email, "password": password})
        if docs:
            return True
        return False

    def retrieve_all_credentials(self):
        return self.get_all_data(self.collection)


if __name__ == "__main__":
    # Connect to MongoDB
    # mongo_handler = MongoDBHandler()
    #
    # collection_name = "credentials"
    #
    # print("List database : ",mongo_handler.list_databases())
    # print("List collection : ",mongo_handler.list_collections())
    #
    # # create collection
    # print("creating collection")
    # mongo_handler.create_collection(collection_name=collection_name)
    # print("List collection : ",mongo_handler.list_collections())
    #
    # # delete collection
    # mongo_handler.delete_collection(collection_name)
    # print("List collection : ",mongo_handler.list_collections())

    # CREDENTIALS COLLECTION
    credential_handler = UserCredentialsHandler()

    # retrieve documents
    print('credentials data : ',credential_handler.retrieve_all_credentials())

    # creating document
    mail_id = "cibin@gmail.com"
    password = "pass"

    message = credential_handler.create_user(mail_id, password)

    print("message : ",message)
    print('credentials data : ', credential_handler.retrieve_all_credentials())

    # retrieve document

    credentials = credential_handler.retrieve_all_credentials()
    print("credentials : ",credentials)

    # CHeck credentials

    is_valid = credential_handler.check_credentials(email="cibin@gmail.com",
                                                    password="pass")
    print("is_valid : ",is_valid)

    is_valid = credential_handler.check_credentials(email="cibin@gmail.com",
                                                    password="pass2")
    print("is_valid : ", is_valid)

