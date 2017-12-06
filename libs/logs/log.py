from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import libs.configs.config_v1 as cfg

class Singleton(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._inst

class Logger(object):

  _logger = None

  def __init__(self):
    if not _logger:
      logger=logging.getLogger("moaskrcnn logger")
      logger.setLevel(logging.DEBUG)
      #set file handle 
      fh = logging.FileHandler(filename=cfg.FLAGS.train_dir+'/maskrcnn.log')
      fh.setLevel(logging.DEBUG)
      
      #set console handle
      ch = logging.StreamHandler()
      ch.setLevel(logging.DEBUG)
      
      formatter = logging.Formatter('[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s')  
      
      fh.setFormatter(formatter)
      ch.setFormatter(formatter)
      
      #add two handle
      logger.addHandler(fh)
      logger.addHandler(ch)

      _logger = logger

  def info(msg):
    _logger.info(msg)

def get_logger():
  logger=logging.getLogger("moaskrcnn logger")
  logger.setLevel(logging.DEBUG)
  #set file handle 
  fh = logging.FileHandler(filename=cfg.FLAGS.train_dir+'/maskrcnn.log')
  fh.setLevel(logging.DEBUG)
  
  #set console handle
  ch = logging.StreamHandler()
  ch.setLevel(logging.DEBUG)
  
  formatter = logging.Formatter('[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s')  
  
  fh.setFormatter(formatter)
  ch.setFormatter(formatter)
  
  #add two handle
  logger.addHandler(fh)
  logger.addHandler(ch)

  return logger

def LOG(mssg):
  logging.basicConfig(filename=cfg.FLAGS.train_dir + '/maskrcnn.log',
                      level=logging.INFO,
                      datefmt='%m/%d/%Y %I:%M:%S %p', format='%(asctime)s %(message)s')
  logging.info(mssg)


if __name__ == '__main__':
  logger = Logger()
  logger.info("fuck")
  logger2 = Logger()
  logger2.info("hehe")
