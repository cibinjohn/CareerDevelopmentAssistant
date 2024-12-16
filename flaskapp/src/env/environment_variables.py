import os



class EnvironmentVariables():

    def __init__(self):

        self.port = os.getenv("PORT", 6999)
        self.host = os.getenv("HOST", "0.0.0.0")
        self.logfile = os.getenv("LOGFILE", "log.txt")



APPCONFIG = EnvironmentVariables()

