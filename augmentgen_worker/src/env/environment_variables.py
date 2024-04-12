import os



class EnvironmentVariables():

    def __init__(self):
        self.augmentation_model_api_port = os.getenv("AUGMENTATION_MODEL_API_PORT", 6997)
        self.augmentation_model_api_host = os.getenv("AUGMENTATION_MODEL_API_HOST", "rag_api")

        self.address_model_api_port = os.getenv("ADDRESS_MODEL_API_PORT", 6998)
        self.address_model_api_host = os.getenv("ADDRESS_MODEL_API_HOST", "addressmodel_api")

        self.usercred_api_port = os.getenv("ADDRESS_MODEL_API_PORT", 6996)
        self.usercred_api_host = os.getenv("ADDRESS_MODEL_API_HOST", "usercred_api")

        self.logfile = os.getenv("LOGFILE", "log/log.txt")


APPCONFIG = EnvironmentVariables()

