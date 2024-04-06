import os

from log.cj_logger import cj_logger


class EnvironmentVariables():

    def __init__(self):

        self.addressing_generator_model_path = os.getenv("ADDRESSING_GENERATOR_MODEL_PATH","CHECKPOINTS/GPT_address_model/address_model_v1")

        self.port = os.getenv("PORT", 6998)
        self.host = os.getenv("HOST", "0.0.0.0")
        self.logfile = os.getenv("LOGFILE", "log.txt")


APPCONFIG = EnvironmentVariables()
