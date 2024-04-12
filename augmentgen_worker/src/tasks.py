from celery import Celery

from log.cj_logger import cj_logger
from utils import call_augmentation_model_api, call_address_model_api

app = Celery('tasks',
             broker='amqp://admin:mypass@rabbit:5672',
             backend='rpc://')


@app.task()
def longtime_add(x, y):
    cj_logger.info('longtime_add Got Request - Starting work ')
    # time.sleep(4)
    cj_logger.info(' longtime_add Work Finished ')
    return x + y

@app.task()
def get_augmentated_response(query, mailid):
    cj_logger.info('get_augmentated_response Got Request - Starting work ')
    cj_logger.info("query : {}. mailid : {}".format(query,mailid))
    # time.sleep(4)
    # result = "dummy augmented answer"
    response = call_augmentation_model_api(query, mailid)
    cj_logger.info("result : {}".format(response))
    cj_logger.info('get_augmentated_response Work Finished ')
    return response

@app.task()
def get_addressing_statement(query):
    cj_logger.info('get_addressing_statement Got Request - Starting work ')
    cj_logger.info("query : {}".format(query))
    # time.sleep(4)
    # result = "dummy augmented answer"
    # response = {"answer":"dummy augmented answer"}
    response = call_address_model_api(query)
    cj_logger.info("response : {}".format(response))
    # response = response['results']
    cj_logger.info('get_addressing_statement Work Finished ')
    return response

@app.task()
def create_credentials(name, mailid, password):
    cj_logger.info('create_credentials Got Request - Starting work ')
    cj_logger.info("name :{}, mailid : {}".format(name, mailid))
    # time.sleep(4)
    # result = "dummy augmented answer"
    # response = {"answer":"dummy augmented answer"}
    # response = call_address_model_api(query)
    response = {
    "code": 200,
    "status": "success",
    "message": "account created"}


    cj_logger.info("response : {}".format(response))

    status = response['status']
    message = response['message']
    # response = response['results']

    cj_logger.info("status : {}, message : {}".format(status, message))
    cj_logger.info('create_credentials Work Finished ')
    return status, message

@app.task()
def validate_credentials(mailid, password):
    cj_logger.info('validate_credentials Got Request - Starting work ')
    cj_logger.info("name :{}, mailid : {}".format(mailid, password))
    # time.sleep(4)
    # result = "dummy augmented answer"
    # response = {"answer":"dummy augmented answer"}
    # response = call_address_model_api(query)
    response = {
    "results": {
        "credentials": {
            "mailid": "user1@gmail.com",
            "password": "pass1"
        },
        "is_account_present": "False"
    },
    "code": 200,
    "message": "Credentials validated successfully"
    }
    cj_logger.info("response : {}".format(response))
    # response = response['results']
    cj_logger.info('validate_credentials Work Finished ')
    return response['results']['is_account_present']