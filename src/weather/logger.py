#Only place where logging is defined, multiple levels and can be used by other modules
from .config import LOG_FILE, LOG_LEVEL_DEFAULT
from loguru import logger
import sys
LOG_FORMAT ='{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}'
CONFIGURED = False

#Logger setup using Loguru library
def setup_logger():
    global CONFIGURED
    if CONFIGURED == True:
        return
    logger.remove()
    logger.add(sys.stderr, level=LOG_LEVEL_DEFAULT, format=LOG_FORMAT)
    logger.add(LOG_FILE, rotation='1 day', retention='1 week', format=LOG_FORMAT)
    CONFIGURED = True
