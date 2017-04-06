import logging

class Log(object):

    def __init__(self,type=logging.DEBUG):
        self.logger = logging.getLogger('vbr')
        hdlr = logging.FileHandler('log/vbr.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr)
        self.logger.setLevel(type)

    def getInstance(self):
        return self.logger