from ctypes import windll
from sys import stderr
from loguru import logger


windll.kernel32.SetConsoleTitleW('Twitter Spammer by Jammer')

logger.remove()
logger.add(
    stderr,
    format='<white>{time:HH:mm:ss}</white>'
           ' | <level>{level: <8}</level>'
           ' - <blue>{message}</blue>',
    filter=lambda record: record["level"].name == "INFO"
)

logger.add(
    stderr,
    format='<white>{time:HH:mm:ss}</white>'
           ' | <level>{level: <8}</level>'
           ' - <red>{message}</red>',
    filter=lambda record: record["level"].name == "ERROR"
)


logger.add(
    stderr,
    format='<white>{time:HH:mm:ss}</white>'
           ' | <level>{level: <8}</level>'
           ' - <green>{message}</green>',
    filter=lambda record: record["level"].name == "SUCCESS"
)



logger.add(
    sink='./files_data/logs.txt',
    format='<white>{time:HH:mm:ss}</white>'
           ' | <level>{level: <8}</level>'
           ' - <white>{message}</white>',
)
