import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self, error_msg, error_info:sys):
        self.error_msg = error_msg
        _,_, exc_tb = error_info.exc_info()
        
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error msg [{2}] ".format(
            self.file_name, self.lineno, str(self.error_msg)
        )

# if __name__ == '__main__':
#     try:
#         logger.logging.info('Enter the try block')
#         a = 1/0
#         print('This will not be printed ',a)
#     except Exception as  e:
#         raise NetworkSecurityException(e,sys)
         