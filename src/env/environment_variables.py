import os

from log.cj_logger import cj_logger


class EnvironmentVariables():

    def __init__(self):

        self.answer_generator_model_path = os.getenv("ANSWER_GENERATOR_MODEL_PATH","CHECKPOINTS/GPT_answer_model/v32")
        self.addressing_generator_model_path = os.getenv("ADDRESSING_GENERATOR_MODEL_PATH","CHECKPOINTS/GPT_address_model/address_model_v1")
        self.chroma_path = os.getenv("CHROMA_PATH", "chroma")

        self.port = os.getenv("PORT", 6999)
        self.host = os.getenv("HOST", "0.0.0.0")
        self.logfile = os.getenv("LOGFILE", "log.txt")

        self.mongodb_port = os.getenv("MONGODB_PORT", 27017)
        self.mongodb_host= os.getenv("MONGODB_HOST", "localhost")
        self.mongodb_name= os.getenv("MONGODB_NAME", "careerdevelopment_db")



        # self.mysql_database_user = os.getenv('db_root_user', 'root')
        # self.mysql_database_password = os.getenv('db_root_password', 'super-secret-password')
        # self.mysql_database_db = os.getenv('db_name', 'HumanActivityPredictionsDB')
        #
        # # self.mysql_database_host = os.getenv('MYSQL_SERVICE_HOST', 'localhost')
        # self.mysql_database_host = os.getenv('MYSQL_SERVICE_HOST', 'localhost')
        # self.mysql_database_port = int(os.getenv('MYSQL_SERVICE_PORT', 3310))

APPCONFIG = EnvironmentVariables()
cj_logger.info("MONGODB_HOST : ".format(APPCONFIG.mongodb_host))
cj_logger.info("MONGODB_PORT : ".format(APPCONFIG.mongodb_port))
