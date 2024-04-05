from datetime import datetime

import pandas as pd
from flask import Flask, request
import uvicorn
from flask_restful import Api, Resource
from flask_cors import CORS

from db.database import UserCredentialsHandler
from env.environment_variables import APPCONFIG
from generator import AugmentedGenerator
from log.cj_logger import cj_logger
from retriever import Retriever

app = Flask(__name__)
CORS(app)

api = Api(app)

retriever = Retriever()

generator = AugmentedGenerator()

credential_handler = UserCredentialsHandler(host=APPCONFIG.mongodb_host,
                                            port=APPCONFIG.mongodb_port,
                                            db_name=APPCONFIG.mongodb_name)

# credential_handler = UserCredentialsHandler()


class Predictor(Resource):
    def get(self):
        return {'message': "Endpoint working successfully..."}

    def put(self):
        input_request = request.get_json()
        cj_logger.info('query : '.format(input_request["query"]))
        #
        matching_docs = retriever.retrieve_top_matching_documents(input_request["query"])

        answer = generator.predict(query=input_request["query"],
                                     matching_docs=matching_docs)
        #
        results = {
            "answer": answer,
            "matching_docs": matching_docs
        }
        cj_logger.info('query : '.format(input_request["query"]))

        return {
                'results': results,
                'code': 200,
                # 'transaction_id':transaction_id,
                'message': "Predictions made successfully..."}


api.add_resource(Predictor, '/chat/response')


class CredentialsValidatorConnector(Resource):

    def get(self):
        input_request = request.get_json()
        # credentials = input_request["credentials"]

        is_account_present = credential_handler.check_credentials(email=input_request.get('mailid'),
                                                                  password=input_request.get("password")
                                                                  )
        is_account_present = str(is_account_present)

        result = {
            "credentials": input_request,
            "is_account_present": is_account_present
        }
        return {'results': result,
                'code': 200,
                # 'transaction_id':transaction_id,
                'message': "Credentials validated successfully"}


api.add_resource(CredentialsValidatorConnector, '/credentials/validate')


class CredentialsCreatorConnector(Resource):

    def put(self):
        input_request = request.get_json()
        # credentials = input_request["credentials"]

        status, message = credential_handler.create_user(email=input_request.get('mailid'),
                                                         password=input_request.get("password")
                                                            )

        return {
                'code': 200,
                'status':status,
                # 'transaction_id':transaction_id,
                'message': message}


api.add_resource(CredentialsCreatorConnector, '/credentials/create')


print(" APPCONFIG.host : ", APPCONFIG.host)
print(" APPCONFIG.port : ", APPCONFIG.port)
#
if __name__ == "__main__":
    # app.run(debug=True, port=APPCONFIG.port, host=APPCONFIG.host)

    uvicorn.run(app)
