import logging
import tools.constant.logging as t_logger

logger = logging.getLogger(__name__)

class Logger:
    def __init__(self) -> None:
        self.create_stream_handler()
    
    def create_stream_handler(self, log_level=logging.WARNING, stream=None): # todo SS: skip typehint check
        handler = logging.StreamHandler(stream)
        handler.setLevel(log_level)
        format = logging.Formatter(t_logger.default_formatter)
        handler.setFormatter(format)


