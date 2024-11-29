from logging import *
# konfiguracja loggera
logger = getLogger(__name__)
logger.setLevel(WARNING)
file_handler = FileHandler('logfile.log')
format = '%(asctime)s : %(levelname)s : %(name)s : %(message)s'
formatter = Formatter(format)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
# u˙ zycie loggera
logger.debug('Rozpoczelismy testowanie dzialania loggera')
logger.info('Do tego miejsca wszystko jest OK')
logger.warning('Cos jest nie tak')
logger.error('Funkcja nie dziala, ale pracujemy dalej')
logger.critical('Blad krytyczny - konczymy dzialanie')