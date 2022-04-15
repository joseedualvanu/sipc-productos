"""
MODULO A
    Description: main module, run other modules

    Args:
		--
    Returns:

    Error:
        --
    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
"""

import datetime
import sys
import os
# Library for logging
# log levels: debug(lowest), info, warning, error, critical(highest)
import logging
# Importo el modulo con el envio de mail ok
from A_Email_ok import enviar_mail_ok

# Obtengo fecha y hora
start_time = datetime.datetime.now()
day = start_time.day
month = start_time.month
year = start_time.year
hour = start_time.hour
minute = start_time.minute
second = start_time.second

# nombres auxiliares
today = str(day)+str(month)+str(year)
hora = str(hour)+':'+str(minute)+':'+str(second)

# direccion y nombres
direction = os.path.dirname(os.path.abspath(__file__))+'/'
nombre_log = direction + "Logs/SIPC_productos_" + str(today) + '.log'
nombre_csv = direction + 'Productos/SIPC_productos_' + str(today) + '.csv'

# private key direction
file_keyP8 = ''

logging.basicConfig(filename= direction + 'SIPC_Productos.log',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
# logging.disable(logging.debug)
logging.debug('Start of program')

nombre_xml = str(today) + '.xml'
# Genero un log de la ejecucion
archivo_log = open(nombre_log, 'a')
archivo_log.write('-------------------------------------\n')
archivo_log.write('Comienzo\t'+ str(hora)+'\n')
archivo_log.write('1- Modulo A_Carga\n')
archivo_log.close()

# Obtengo la lista de productos desde SOAP
from B_Productos import productos
(lista_prod) = productos(direction,nombre_log,nombre_csv)

# # Obtengo la lista de productos desde SOAP
from C_Snowflake import carga_snow
sql2 = carga_snow(direction,nombre_log,lista_prod,file_keyP8)

logging.debug('End of program')

# Notificacion por mail OK
# enviar_mail_ok(nombre_log)
