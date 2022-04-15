"""
MODULO B
    Description:

    Args:
		--
    Returns:

    Error:
        --
    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
"""

def productos(direction,nombre_log,nombre_csv):

    archivo_log = open(nombre_log, 'a')
    archivo_log.write('2- Modulo B_Productos\n')

    # Importo el modulo con el envio de mail
    from A_Error_Handling import enviar_mail_error
    import requests
    # Liberia para salir del flujo
    import sys
    import csv
    from bs4 import BeautifulSoup

    # Servicio para declarar
    URL = ""

    headers = {'content-type': 'text/xml'}

    obtenerCodigosProductos= '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:int="http://interfaces.ws.sipc.bullseye.com.uy/">
       <soapenv:Header/>
       <soapenv:Body>
          <int:obtenerProductos/>
       </soapenv:Body>
    </soapenv:Envelope>'''

    try:
        r = requests.post(url = URL,data=obtenerCodigosProductos,headers=headers, timeout = 600)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:" + str(errh))
        archivo_log.write("Http Error:" + str(errh)+"\n")
        archivo_log.write('-------------------------------------\n')
        archivo_log.close()
        enviar_mail_error(nombre_log)
        sys.exit()
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:" + str(errc))
        archivo_log.write("Error Connecting:" + str(errc)+'\n')
        archivo_log.write('-------------------------------------\n')
        archivo_log.close()
        enviar_mail_error(nombre_log)
        sys.exit()
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:" + str(errt))
        archivo_log.write("Timeout Error:" + str(errt)+'\n')
        archivo_log.write('-------------------------------------\n')
        archivo_log.close()
        enviar_mail_error(nombre_log)
        sys.exit()
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else" + str(err))
        archivo_log.write("OOps: Something Else" + str(err)+'\n')
        archivo_log.write('-------------------------------------\n')
        archivo_log.close()
        enviar_mail_error(nombre_log)
        sys.exit()

    string_xml = r.content
    # parser = ET.XMLParser(encoding="ISO-8859-1")
    # parser = ET.XMLParser(encoding="utf-8")
    # parser = ET.XMLParser(encoding="utf-16")
    # tree = ET.fromstring(r.content, parser)
    # print(tree.findall('<nombre>'))

    soup = BeautifulSoup(string_xml, 'xml')

    lista_prod = list()

    for cod_bar in soup.findAll('return'):
        lista_prod.append("\'"+cod_bar.find('codigo_barra').text+"\'"+','+cod_bar.find('interno').text+','+"\'"+cod_bar.find('nombre').text+"\'")

    # Guardo los productos en un csv
    file = open(nombre_csv, 'w+', newline ='')

    with file:
        write = csv.writer(file,delimiter='\n')
        write.writerow(lista_prod)

    print(r.reason)
    print(r.status_code)

    return lista_prod
