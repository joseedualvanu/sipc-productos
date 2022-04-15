def enviar_mail_ok(nombre_log):

    # importamos la libreria smtplib (no es necesario instalarlo)
    import smtplib
    # importamos librerias  para construir el mensaje
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    #importamos librerias para adjuntar
    from email.mime.base import MIMEBase
    from email import encoders

    # definimos los correo de remitente y receptor
    #se envia un mail a
    addr_to   = ['']
    #el mail sale desde el correo
    addr_from = ''

    # Define SMTP email server details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    # Usuario de BI
    smtp_user   = ''
    smtp_pass   = ''

    # Construimos el mail
    msg = MIMEMultipart()
    msg['To'] = ', '.join(addr_to)
    msg['From'] = 'Equipo de BI - PDI'
    msg['Subject'] = 'OK - Proceso Automatizacion SIPC Productos'
    #cuerpo del mensaje en HTML y si fuera solo text puede colocar en el 2da parametro 'plain'
    # msg.attach(MIMEText('<h1>Verificar proceso< p>cuerpo de mensaje','html'))
    msg.attach(MIMEText('Todo ok.','plain'))

    #adjuntamos fichero de texto pero puede ser cualquer tipo de archivo
    #cargamos el archivo a adjuntar
    fp = open(nombre_log,'rb')
    adjunto = MIMEBase('multipart', 'encrypted')
    #lo insertamos en una variable
    adjunto.set_payload(fp.read())
    fp.close()
    #lo encriptamos en base64 para enviarlo
    encoders.encode_base64(adjunto)
    #agregamos una cabecera y le damos un nombre al archivo que adjuntamos puede ser el mismo u otro
    adjunto.add_header('Content-Disposition', 'attachment', filename="Registro_SIPC_Productos.log")
    #adjuntamos al mensaje
    msg.attach(adjunto)

    # inicializamos el stmp para hacer el envio
    server = smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    #logeamos con los datos ya seteamos en la parte superior
    server.login(smtp_user,smtp_pass)
    #el envio
    server.sendmail(addr_from, addr_to, msg.as_string())
    #apagamos conexion stmp
    server.quit()
