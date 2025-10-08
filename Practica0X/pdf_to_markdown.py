"""
Script para convertir PDF a README.md
Extrae texto e imágenes del PDF "INSTALACIÓN DE AIRFLOW EN LA RASPBERRY PI 3.pdf"
y genera un README.md estructurado con formato GitHub profesional
"""

import os
import fitz  # PyMuPDF
from pathlib import Path

def extraer_contenido_pdf(ruta_pdf: str, directorio_salida: str = "."):
    """
    Extrae texto e imágenes de un PDF
    """
    print(f"🔄 Procesando PDF: {ruta_pdf}")
    
    # Crear directorio para imágenes
    dir_imagenes = os.path.join(directorio_salida, "imagenes")
    Path(dir_imagenes).mkdir(exist_ok=True)
    
    # Abrir PDF
    doc = fitz.open(ruta_pdf)
    
    contenido_texto = []
    imagenes_extraidas = []
    
    for num_pagina in range(len(doc)):
        pagina = doc[num_pagina]
        
        # Extraer texto
        texto_pagina = pagina.get_text()
        if texto_pagina.strip():
            contenido_texto.append(f"## Página {num_pagina + 1}\n\n{texto_pagina}\n")
        
        # Extraer imágenes
        lista_imagenes = pagina.get_images()
        
        for img_index, img in enumerate(lista_imagenes):
            xref = img[0]
            imagen_dict = doc.extract_image(xref)
            imagen_data = imagen_dict["image"]
            extension = imagen_dict["ext"]
            
            # Guardar imagen
            nombre_imagen = f"imagen_pagina_{num_pagina + 1}_{img_index + 1}.{extension}"
            ruta_imagen = os.path.join(dir_imagenes, nombre_imagen)
            
            with open(ruta_imagen, "wb") as archivo_imagen:
                archivo_imagen.write(imagen_data)
            
            imagenes_extraidas.append({
                "nombre": nombre_imagen,
                "pagina": num_pagina + 1,
                "ruta": f"imagenes/{nombre_imagen}"
            })
            
            print(f"📷 Imagen extraída: {nombre_imagen}")
    
    doc.close()
    
    return contenido_texto, imagenes_extraidas

def generar_readme(texto_contenido: list, imagenes: list, archivo_salida: str = "README_AIRFLOW.md"):
    """
    Genera README.md con formato profesional
    """
    
    readme_content = """<div align="center">

# 🚁 **Instalación de Apache Airflow en Raspberry Pi 3**

## **Guía Completa de Configuración y Deployment**

**Tutorial paso a paso para instalar y configurar Apache Airflow en Raspberry Pi 3, incluyendo configuración del entorno, dependencias y optimizaciones específicas para hardware ARM.**

![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-3-red?style=for-the-badge&logo=raspberry-pi&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.0+-blue?style=for-the-badge&logo=apache-airflow&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python&logoColor=white)

</div>

---

## 📋 **Contenido**
- [🎯 Descripción](#-descripción)
- [📋 Requisitos](#-requisitos)
- [🔧 Instalación](#-instalación)
- [⚙️ Configuración](#️-configuración)
- [🚀 Puesta en Marcha](#-puesta-en-marcha)
- [📸 Capturas de Pantalla](#-capturas-de-pantalla)
- [🔧 Solución de Problemas](#-solución-de-problemas)
- [📝 Conclusiones](#-conclusiones)

## 🎯 **Descripción**

Este documento proporciona una guía detallada para instalar **Apache Airflow** en una **Raspberry Pi 3**. Apache Airflow es una plataforma de código abierto para desarrollar, programar y monitorear flujos de trabajo programáticamente.

### **¿Por qué Airflow en Raspberry Pi?**
- **💰 Costo eficiente:** Ideal para proyectos personales y aprendizaje
- **🔋 Bajo consumo:** Perfecto para ejecutar 24/7
- **🎓 Educativo:** Excelente para aprender conceptos de orquestación
- **🏠 Self-hosted:** Control total sobre tus datos y procesos

"""

    # Agregar contenido extraído del PDF
    readme_content += "\n## 📖 **Contenido del Tutorial**\n\n"
    
    for i, texto in enumerate(texto_contenido):
        # Limpiar y formatear el texto
        texto_limpio = texto.replace("## Página", "### Sección")
        readme_content += texto_limpio + "\n"
    
    # Agregar sección de imágenes
    if imagenes:
        readme_content += "\n## 📸 **Capturas de Pantalla**\n\n"
        readme_content += "A continuación se muestran las imágenes del proceso de instalación:\n\n"
        
        for i, img in enumerate(imagenes):
            readme_content += f"### Imagen {i + 1} - Página {img['pagina']}\n\n"
            readme_content += f"![Instalación Airflow - Imagen {i + 1}]({img['ruta']})\n\n"
    
    # Agregar conclusiones y footer
    readme_content += """
## 🔧 **Solución de Problemas Comunes**

### **Error de memoria insuficiente**
```bash
# Aumentar swap
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile
# Cambiar CONF_SWAPSIZE=1024
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```

### **Dependencias faltantes**
```bash
# Instalar dependencias del sistema
sudo apt-get update
sudo apt-get install -y python3-dev libffi-dev libssl-dev
```

## 📝 **Conclusiones**

La instalación de **Apache Airflow** en **Raspberry Pi 3** es una excelente manera de:

- **🎓 Aprender** conceptos de orquestación de workflows
- **💰 Crear** un entorno de desarrollo económico
- **🔬 Experimentar** con pipelines de datos
- **🏠 Implementar** soluciones self-hosted

### **🎯 Beneficios Logrados:**
- ✅ **Entorno funcional** de Airflow en hardware ARM
- ✅ **Configuración optimizada** para recursos limitados
- ✅ **Base sólida** para proyectos de automatización
- ✅ **Conocimiento práctico** de deployment en dispositivos IoT

<div align="center">

---

### 🎯 **¡Dale una estrella si te ayudó esta guía!** ⭐

**Creado con ❤️ para la comunidad Raspberry Pi y Apache Airflow**

</div>
"""
    
    # Guardar archivo
    with open(archivo_salida, 'w', encoding='utf-8') as archivo:
        archivo.write(readme_content)
    
    print(f"✅ README generado: {archivo_salida}")
    return archivo_salida

def main():
    """Función principal"""
    ruta_pdf = "INSTALACIÓN DE AIRFLOW EN LA RASPBERRY PI 3.pdf"
    
    if not os.path.exists(ruta_pdf):
        print(f"❌ Error: No se encontró el archivo {ruta_pdf}")
        return
    
    print("🚀 Iniciando conversión PDF a README.md...")
    
    try:
        # Extraer contenido
        texto, imagenes = extraer_contenido_pdf(ruta_pdf)
        
        # Generar README
        archivo_readme = generar_readme(texto, imagenes)
        
        print("\n" + "="*60)
        print("🎉 CONVERSIÓN COMPLETADA EXITOSAMENTE")
        print("="*60)
        print(f"📄 README generado: {archivo_readme}")
        print(f"📷 Imágenes extraídas: {len(imagenes)}")
        print("📁 Archivos en carpeta 'imagenes/'")
        print("="*60)
        
    except ImportError:
        print("❌ Error: PyMuPDF no está instalado")
        print("Instala con: pip install PyMuPDF")
    except Exception as e:
        print(f"❌ Error durante la conversión: {e}")

if __name__ == "__main__":
    main()