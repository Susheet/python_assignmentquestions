import logging

# These are the 5 levels of logging and they go in least to most important order.
# logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging.critical()

logging.basicConfig(filename='test.log', filemode="w", level=logging.DEBUG)  # we can specify the level of logging we want to see in the output and also the filemode
# filemode = "w" will overwrite the file everytime we run the code
# logging.basicConfig(filename='test.log', filemode="w", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')  # we can also specify the format of the output

logging.debug("debug")
logging.info("info")
logging.warning("warning")  # by default we get output for warning and above
logging.error("error")
logging.critical("critical")

# output
# WARNING:root:warning
# ERROR:root:error  
# CRITICAL:root:critical 
# we can see that the output is in the format of level:logger_name:message  and the logger_name is root by default

