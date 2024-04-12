# import requests
# import json
#
# from env.environment_variables import APPCONFIG
# from log.cj_logger import cj_logger
# from wsgi import address_model_celery_app
#
#
#
# def get_addressing_statement(query):
#     cj_logger.info("Calling get_addressing_statement API")
#     url = "http://{}:{}/chat/response".format(APPCONFIG.address_model_host,
#                                               APPCONFIG.address_model_port)
#     cj_logger.info("url : {}".format(url))
#     cj_logger.info("query : {}".format(query))
#
#     payload = json.dumps({
#         "query": query
#     })
#     headers = {
#         'Content-Type': 'application/json'
#     }
#     answer = "Here is the answer to your question.\n"
#     try:
#         response = requests.request("PUT", url, headers=headers, data=payload)
#         answer = response.json()
#         answer = answer['results']['answer']
#
#     except Exception as err:
#         cj_logger.error("Problem with connecting to the addressing model API")
#         cj_logger.error(err)
#     cj_logger.info("get_addressing_statement end")
#
#     return answer
#
# if __name__ == "__main__":
#
#     resp = get_addressing_statement("How to become an engineer?")
#     print(resp)