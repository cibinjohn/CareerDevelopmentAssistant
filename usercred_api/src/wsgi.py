from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource

from db.database import UserCredentialsHandler, UserConversationHandler
from env.environment_variables import APPCONFIG
from log.cj_logger import cj_logger

app = Flask(__name__)
CORS(app)

api = Api(app)


credential_handler = UserCredentialsHandler(host=APPCONFIG.mongodb_host,
                                            port=APPCONFIG.mongodb_port,
                                            db_name=APPCONFIG.mongodb_name)

conversation_handler = UserConversationHandler(host=APPCONFIG.mongodb_host,
                                               port=APPCONFIG.mongodb_port,
                                               db_name=APPCONFIG.mongodb_name)




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
