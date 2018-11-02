import coloredlogs, logging

logger = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG')

coloredlogs.install(level='DEBUG', logger=logger)

logger.debug("this is a debugging message")
logger.info("this is an informational message")
logger.warning("this is a warning message")
logger.error("this is an error message")
logger.critical("this is a critical message")
