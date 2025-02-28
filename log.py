import sys
from logging import (StreamHandler, FileHandler, Formatter,
                     getLogger, DEBUG)


# class HandlerForGui(Handler):

#     def emit(self, record: LogRecord) -> None:
#         log_entry = self.format(record)


formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = getLogger('logger')
logger.setLevel(DEBUG)
handler = StreamHandler(stream=sys.stdout)
file_handler = FileHandler(filename="log.log", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(handler)
logger.addHandler(file_handler)
