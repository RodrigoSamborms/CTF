<h1 align="center"># Proyecto primera parte</h1>
<img src="imagenes/N8Nlogo.png" alt="Docker" width="400">

### EL LISTADO DE COMANDO PARA INSTALAR LO ENCONTRARA EN LA CARPETA DE DOCUMENTOS COMO n8n_instalacio.txt se muestra el proceso de instalacion para un ambiente WSL Debian 12

## PRIMERO ACTUALICE EL SISTEMA

![alt text](./imagenes/n8n_B01.jpg)

## INSTALE NODE.JS
![alt text](./imagenes/n8n_B02.jpg)
use nvm (nodejs version manager)
![alt text](./imagenes/n8n_B03.jpg)
Revise la instalación

![alt text](./imagenes/n8n_B04.jpg)

## INSTALAR N8N GLOBALMENTE

![alt text](./imagenes/n8n_B05.jpg)
Esto tomara algo de tiempo en completarse, algunos paquetes fallaran, pero la instalación continuara sin problemas.
Al terminar verifique la instalación
![alt text](./imagenes/n8n_B06.jpg)
Incie el servicio n8n
![alt text](./imagenes/n8n_B07.jpg)
Acceda a la interfaz
![alt text](./imagenes/n8n_B08.jpg)
Tras completar el proceso de registro estara listo para crear sus Flujos de Trabajo
![alt text](./imagenes/n8n_B09.jpg)

<h1 align="center"># Instalar LibreOffice</h1>
<img src="imagenes/LibreOffice_logo.png" alt="Libreoffice" width="400">

Utilizaremos la paqueteria LibreOffice para automatizar la conversion de archivos editables docx a pdf.
## Actualizar el sistema:    
    sudo apt update
    sudo apt upgrade
![alt text](./imagenes/n8n_A01.jpg)
## Instalar el paquete del repo de Debian
    sudo apt install libreoffice
![alt text](./imagenes/n8n_A02.jpg)
## Verificar la instalacion
    libreoffice --version
![alt text](./imagenes/n8n_A03.jpg)
## Instalar ambiente de Java (Opcional)
    sudo apt install default-jre
![alt text](./imagenes/n8n_A04.jpg)  
## Ejecutar la aplicacion
Escriba el siguiente comando en el terminal como indica (A)

      libreoffice

Podra ver que se ejecuta la GUI del progama 
![alt text](./imagenes/n8n_A05.jpg) 


