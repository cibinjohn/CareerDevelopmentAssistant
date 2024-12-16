import logging

cj_logger = logging.getLogger('cj_logger')
cj_logger.setLevel(logging.DEBUG)

#formate of output
cj_formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')

#file handler
file_handler = logging.FileHandler(filename="cj_log.txt")
file_handler.setFormatter(cj_formatter)

# std out
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(cj_formatter)


cj_logger.addHandler(file_handler)
cj_logger.addHandler(stream_handler)