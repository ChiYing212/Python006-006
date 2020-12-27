import logging

def timeLogging():
    logging.basicConfig(filename="/var/log/python-201227/week01_zoey.log", 
                        level=logging.DEBUG,
                        format="%(message)s : %(asctime)s") 
    
    logging.debug("debug message")

timeLogging()