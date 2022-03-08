import logging
import sys
logger = logging.getLogger('server')

"""
Реализовать дескриптор для класса серверного сокета, а в нем — проверку номера порта.
Это должно быть целое число (>=0). Значение порта по умолчанию равняется 7777. 
Дескриптор надо создать в отдельном классе. 
Его экземпляр добавить в пределах класса серверного сокета. 
Номер порта передается в экземпляр дескриптора при запуске сервера.
"""

if sys.argv[0].find('client') == -1:
    logger = logging.getLogger('server')
else:
    logger = logging.getLogger('client')


class Port:
    def __set__(self, instance, value):
        if not 1023 < value < 65536:
            logger.critical(
                f'Вы указали номер порта: {value}. Номер порта может находиться в промежутке от 1024 до 65535.')
            exit(1)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
