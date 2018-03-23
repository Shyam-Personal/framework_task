import logging
import os

class update_log(object):
    def __init__(self, path, log_file_name):
        self.path = path
        self.log_file_name = log_file_name
    
    def setup_log(self, level="INFO"):
        try:
            if not os.path.exists(os.path.join(self.path, "Log")):
                os.mkdir(os.path.join(self.path, "Log"))
            log_path = os.path.join(self.path, "Log", self.log_file_name)
            logger = logging.getLogger("mylog")
            logger.setLevel(level)
            handler = logging.FileHandler(log_path)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            
            return logger
        except Exception as e:            
            return "Exception in set up log" + e

    def write_log(self, logger, level, message):
        getattr(logger, level)(message)
    
if __name__ == "__main__":
    log = update_log(os.getcwd(), "test.log")
    lh = log.setup_log()
    log.write_log(lh, "info", "testing")