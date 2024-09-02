import logging

# Configure the logging system
logging.basicConfig(level=logging.DEBUG)

# Create a logger
logger = logging.getLogger('MyApp')
logger.propagate = False

infoFileHandler = logging.FileHandler('info.log')
infoFileHandler.setLevel(level='INFO')

criticalFileHandler = logging.FileHandler('critical.log')
criticalFileHandler.setLevel(level='CRITICAL')

logger.addHandler(infoFileHandler)
logger.addHandler(criticalFileHandler)

# Log some messages
logger.debug('This is a debug message')
logger.log('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
