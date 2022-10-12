import logging

logging.getLogger().setLevel(logging.NOTSET)
logger = logging.getLogger()

logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename="./server.log")
formatter_stream = logging.Formatter(
    "%(module)s - %(funcName)s - line:%(lineno)d - %(levelname)s - %(message)s"
)

formatter_file = logging.Formatter(
    "%(asctime)s - %(module)s - %(funcName)s - line:%(lineno)d - %(levelname)s - %(message)s"
)
ch.setFormatter(formatter_stream)
fh.setFormatter(formatter_file)
logger.addHandler(ch)
logger.addHandler(fh)
