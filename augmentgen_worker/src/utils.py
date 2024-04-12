import requests
import json

from log.cj_logger import cj_logger
from env.environment_variables import APPCONFIG


def call_augmentation_model_api(query, mailid):
    url = "http://{}:{}/chat/response".format(APPCONFIG.augmentation_model_api_host,
                                              APPCONFIG.augmentation_model_api_port)

    cj_logger.info("call_augmentation_model_api url : {}".format(url))

    payload = json.dumps({
        "query": query,
        "mailid": mailid
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    cj_logger.info("response.text : {}".format(response.text))

    return response.json()['results']


def call_address_model_api(query):
    url = "http://{}:{}/chat/response".format(APPCONFIG.address_model_api_host,
                                              APPCONFIG.address_model_api_port)

    cj_logger.info("call_address_model_api url : {}".format(url))

    payload = json.dumps({
        "query": query
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    cj_logger.info("call_address_model_api response.text : {}".format(response.text))

    return response.json()['results']


def call_create_credentials_api(name, mailid, password):

    url = "http://{}:{}/credentials/create".format(APPCONFIG.usercred_api_host,
                                                   APPCONFIG.usercred_api_port)

    cj_logger.info("call_create_credentials_api url : {}".format(url))

    payload = json.dumps({
        "name": name,
        "mailid": mailid,
        "password": password

    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    cj_logger.info("call_create_credentials_api response.text : {}".format(response.text))

    return response.json()

def call_validate_credentials_api(mailid, password):

    url = "http://{}:{}/credentials/validate".format(APPCONFIG.usercred_api_host,
                                                   APPCONFIG.usercred_api_port)

    cj_logger.info("call_validate_credentials_api url : {}".format(url))

    payload = json.dumps({
        "mailid": mailid,
        "password": password

    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    cj_logger.info("call_validate_credentials_api response.text : {}".format(response.text))

    return response.json()
