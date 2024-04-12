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