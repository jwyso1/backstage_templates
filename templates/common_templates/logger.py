import logging
import tools.constants.logging as t_constants
import tools.protocols.logging as t_protocols

logger = logging.getLogger(__name__)


class Logger:
    def __init__(self) -> None:
        self.create_stream_handler()

    @staticmethod
    def create_stream_handler(
        log_level: int = logging.WARNING,
        stream: t_protocols.LoggingStream | None = None,
    ):
        handler = logging.StreamHandler(stream)
        handler.setLevel(log_level)
        format = logging.Formatter(t_constants.DEFAULT_FORMATTER)
        handler.setFormatter(format)
