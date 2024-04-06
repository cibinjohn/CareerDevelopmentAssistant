from datetime import datetime

import pandas as pd
from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS

from env.environment_variables import APPCONFIG
from generator import QuestionAddressingGenerator
from log.cj_logger import cj_logger

app = Flask(__name__)
CORS(app)

api = Api(app)

generator = QuestionAddressingGenerator()


class Predictor(Resource):
    def get(self):
        return {'message': "Endpoint working successfully..."}

    def put(self):
        input_request = request.get_json()
        cj_logger.info("Predictor : input_request : {}".format(input_request))
        cj_logger.info('query : '.format(input_request["query"]))
        cj_logger.info("Generating augmented response...")
        answer = generator.get_addressing_statement(query=input_request["query"])


        results = {
            "answer": answer,
        }
        cj_logger.info('query : '.format(input_request["query"]))

        return {
                'results': results,
                'code': 200,
                # 'transaction_id':transaction_id,
                'message': "Predictions made successfully..."}


api.add_resource(Predictor, '/chat/response')


print(" APPCONFIG.host : ", APPCONFIG.host)
print(" APPCONFIG.port : ", APPCONFIG.port)
#
if __name__ == "__main__":

    app.run(debug=True, port=APPCONFIG.port, host=APPCONFIG.host)
