import logging
import logging.handlers

#создаем объект-логгер с именем server.main
logger = logging.getLogger('server.main')

#создаем объект форматирования "<дата-время> <уровень_важности> <имя_модуля> <сообщение>
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")

#создаем файловый обработчик логирования
# .TimedRotatingFileHandler
# fh = logging.TimedRotatingFileHandler('server.main.log', when = 'M', interval = 1, encoding = 'utf-8', backupCount=2)
fh = logging.handlers.TimedRotatingFileHandler('server.main.log', when = 'midnight', interval = 1, encoding = 'utf-8', backupCount=2)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

#Добавляем в логгер наш обработчик событий
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # Создаем потоковый обработчик логирования (по умолчанию sys.stderr):
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.info('Тестовый запуск логирования server')