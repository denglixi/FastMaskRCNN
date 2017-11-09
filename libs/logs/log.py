from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import libs.configs.config_v1 as cfg

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
