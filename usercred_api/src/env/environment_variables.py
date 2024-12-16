import os

from log.cj_logger import cj_logger


class EnvironmentVariables():

    def __init__(self):

        self.port = os.getenv("PORT", 6996)
        self.host = os.getenv("HOST", "0.0.0.0")
        self.logfile = os.getenv("LOGFILE", "log.txt")

        self.mongodb_port = os.getenv("MONGODB_PORT", 27017)
        self.mongodb_host= os.getenv("MONGODB_HOST", "localhost")
        self.mongodb_name= os.getenv("MONGODB_NAME", "careerdevelopment_db")


APPCONFIG = EnvironmentVariables()
cj_logger.info("MONGODB_HOST : ".format(APPCONFIG.mongodb_host))
cj_logger.info("MONGODB_PORT : ".format(APPCONFIG.mongodb_port))
