# from flask import Flask
# from celery import Celery
#


from datetime import datetime

from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
from celery import Celery

from env.environment_variables import APPCONFIG
from log.cj_logger import cj_logger

app = Flask(__name__)
CORS(app)

api = Api(app)

augmentation_model_celery_app = Celery('simple_worker',
                    broker='amqp://admin:mypass@rabbit:5672',
                    backend='rpc://')

# Print the list of registered tasks
cj_logger.info("Registered tasks:")
for task_name, task_func in augmentation_model_celery_app.tasks.items():
    cj_logger.info(f"Task Name: {task_name}, Task Function: {task_func}")
class Predictor(Resource):
    def get(self):
        return {'message': "Endpoint working successfully..."}

    def put(self):
        input_request = request.get_json()
        cj_logger.info("Predictor : input_request : {}".format(input_request))
        cj_logger.info('query : '.format(input_request["query"]))

        # Print the list of registered tasks
        cj_logger.info("Registered tasks:")
        query = input_request['query']
        mailid = input_request['mailid']

        # answer = generator.get_addressing_statement(query=input_request["query"])
        # answer = augmentation_model_celery_app.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
        answer = augmentation_model_celery_app.send_task('tasks.get_augmentated_response', kwargs={'query': query,
                                                                                                   'mailid': mailid})
        task_id = answer.id
        results = answer.get()
        # cj_logger.info('results : '.format(results))
        #
        # results = results['results']

        # results = {
        #     "answer": answer,
        # }
        cj_logger.info('results : '.format(results))

        return {
                'results': results,
                'code': 200,
                'transaction_id':task_id,
                'message': "Predictions made successfully..."}


api.add_resource(Predictor, '/chat/response')

#
if __name__ == "__main__":
    cj_logger.info("port : {}".format(APPCONFIG.port))
    app.run(debug=True, port=APPCONFIG.port, host=APPCONFIG.host)


#