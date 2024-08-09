import logging

# Configure the logging system
logging.basicConfig(level=logging.DEBUG)
# Create a logger
logger = logging.getLogger('MyApp')
logger.propagate = False #Set to True get console logs via rootlogger


# crete and add handlers for each environment/destination
intFileHandler = logging.FileHandler('INT.log')
stagFileHandler = logging.FileHandler('STAG.log')
prodFileHandler = logging.FileHandler('PROD.log')

logger.addHandler(intFileHandler)
logger.addHandler(stagFileHandler)
logger.addHandler(prodFileHandler)

# Define filters

def filter_log_int_messages(record):
    if 'INT' in record.msg:
        return True
    return False

def filter_log_stag_messages(record):
    if 'STAG' in record.msg:
        return True
    return False

def filter_log_prod_messages(record):
    if 'PROD' in record.msg:
        return True
    return False

intFileHandler.addFilter(filter_log_int_messages)
stagFileHandler.addFilter(filter_log_stag_messages)
prodFileHandler.addFilter(filter_log_prod_messages)

print(logger.level)

# Log some messages
# Only Messages containing the string 'INT' should go the INT.log file
# Only Messages containing the string 'STAG' should go the STAG.log file
# Only Messages containing the string 'PROD' should go the PROD.log file
logger.info('This is an INT message1')
logger.info('This is a STAG message1')
logger.info('This is a PROD message1')
logger.info('This is an PROD message2')
logger.info('This is an INT message2')
logger.info('This is an INT message3')
logger.info('This is a STAG message2')
logger.info('This is a PROD message3')
logger.info('This is an PROD message4')
logger.info('This is an INT message4')
