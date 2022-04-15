"""
MODULO C
    Description:

    Args:
		--
    Returns:

    Error:
        --
    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
"""

def carga_snow(direction,nombre_log,lista_prod,file_keyP8):
    # Liberia para salir del flujo
    import sys

    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives.asymmetric import dsa
    from cryptography.hazmat.primitives import serialization

    # Importo el modulo con el envio de mail
    from A_Error_Handling import enviar_mail_error
    # Snowflake
    from snowflake import connector

    import datetime

    archivo_log = open(nombre_log, 'a')
    archivo_log.write('3- Modulo C_Snowflake\n')

    # Paso a str la lista de prod para usarlo en el sql
    lista_prod_str = "),\n(".join(lista_prod)
    # print("(" + lista_prod_str + ")")

    with open(file_keyP8, "rb") as key:
        p_key= serialization.load_pem_private_key(
            key.read(),
            password=None,
            backend=default_backend()
        )
    pkb = p_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption())

    # Realizo la conexion con snowflake
    try:
        conn = connector.connect(
            user='python',
            account='dp32414.us-east-1',
            private_key= pkb,
            warehouse='COMPUTE_WH',
            database='MSTRDB',
            schema='public'
            )

        #create cursor1
        curs1 = conn.cursor()
        #create cursor2
        curs2=conn.cursor()

    except:
        print('No se pudo lograr la conexión con Snowflake')
        archivo_log.write('No se pudo lograr la conexión con Snowflake\n')
        archivo_log.write('-------------------------------------\n')
        archivo_log.close()
        enviar_mail_error(nombre_log)
        sys.exit()

    # Consulta SQL
    sql1 = '''

    '''

    sql2 = '''
    INSERT INTO TABLA
    VALUES''' + "(" + lista_prod_str + ")" + ";"

    # print(sql1)
    # print(sql2)

    try:
        curs1.execute(sql1)
    except:
        print('Problemas con la ejecución de la consulta SQL1')
        archivo_log.write('Problemas con la ejecución de la consulta SQL\n')
        archivo_log.write(str(curs1)+'\n')
        archivo_log.write('-------------------------------------\n')
        archivo_log.close()
        enviar_mail_error(nombre_log)
        sys.exit()

    try:
        curs2.execute(sql2)
    except:
        print('Problemas con la ejecución de la consulta SQL2')
        archivo_log.write('Problemas con la ejecución de la consulta SQL\n')
        archivo_log.write(str(curs2)+'\n')
        archivo_log.write('-------------------------------------\n')
        archivo_log.close()
        enviar_mail_error(nombre_log)
        sys.exit()

    # Obtengo fecha y hora de finalizacion
    start_time = datetime.datetime.now()

    hour = start_time.hour
    minute = start_time.minute
    second = start_time.second

    hora = str(hour)+':'+str(minute)+':'+str(second)

    print("Proceso OK")
    archivo_log.write('Fin\t\t'+ str(hora)+'\n')
    archivo_log.write('-------------------------------------\n')
    archivo_log.close()

    # Cierro la conexion
    curs1.close()
    curs2.close()
