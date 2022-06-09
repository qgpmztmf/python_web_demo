import os
import logging

class Hello():
    def __init__(self):
        set_log_config()

    def hello(self):
        logging.info("Test")


def set_log_config():
    LOG_FORMAT = "[%(asctime)s] - %(levelname)s - %(filename)s[line:%(lineno)d] - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    logging.basicConfig(level='INFO', format=LOG_FORMAT, datefmt=DATE_FORMAT)


if __name__ == '__main__':
    set_log_config()
    h = Hello()
    h.hello()
