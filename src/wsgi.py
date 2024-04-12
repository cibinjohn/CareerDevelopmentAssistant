from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource

from db.database import UserCredentialsHandler, UserConversationHandler
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

conversation_handler = UserConversationHandler(host=APPCONFIG.mongodb_host,
                                               port=APPCONFIG.mongodb_port,
                                               db_name=APPCONFIG.mongodb_name)



# credential_handler = UserCredentialsHandler()


class Predictor(Resource):
    def get(self):
        return {'message': "Endpoint working successfully..."}

    def put(self):
        input_request = request.get_json()
        cj_logger.info("Predictor : input_request : {}".format(input_request))
        cj_logger.info('query : '.format(input_request["query"]))

        mailid = input_request['mailid']
        query = input_request["query"]

        cj_logger.info("Adding query to the mongodb conversation collection...")
        conversation_handler.add_conversation(email=mailid,
                                              statement=query,
                                              statement_type="query")
        #
        cj_logger.info("Retreiving matching docs")
        matching_docs = retriever.retrieve_top_matching_documents(query)
        cj_logger.info("Matching docs : {}".format(matching_docs))
        # answer = "dummy_answer"
        cj_logger.info("Generating augmented response...")
        answer, is_present = generator.predict(query=input_request["query"],
                                   matching_docs=matching_docs)

        results = {
            "answer": answer,
            "is_augmented": is_present,
            "matching_docs": matching_docs
        }
        cj_logger.info('results : '.format(results))

        cj_logger.info("Adding response to the mongodb conversation collection...")
        conversation_handler.add_conversation(email=mailid,
                                              statement=answer,
                                              statement_type="response")

        return {
            'results': results,
            'code': 200,
            # 'transaction_id':transaction_id,
            'message': "Predictions made successfully..."}


api.add_resource(Predictor, '/chat/response')


class CredentialsValidatorConnector(Resource):

    def put(self):
        input_request = request.get_json()
        # credentials = input_request["credentials"]
        cj_logger.info("CredentialsValidatorConnector : input_request : {}".format(input_request))
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
        cj_logger.info("CredentialsCreatorConnector : input_request : {}".format(input_request))

        status, message = credential_handler.create_user(email=input_request.get('mailid'),
                                                         password=input_request.get("password")
                                                         )

        return {
            'code': 200,
            'status': status,
            # 'transaction_id':transaction_id,
            'message': message}


api.add_resource(CredentialsCreatorConnector, '/credentials/create')


if __name__ == "__main__":
    # app.run(debug=True, port=APPCONFIG.port, host=APPCONFIG.host)

    app.run(debug=True, port=APPCONFIG.port, host=APPCONFIG.host)
