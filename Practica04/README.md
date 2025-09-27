<div align="center">

# 🚀 **Prefect aplicado al manejo de archivos JSON**

## **Pipeline de Procesamiento de Datos con JSONPlaceholder**

**Demostración completa del uso de Prefect para crear pipelines robustos de procesamiento de datos JSON, incluyendo obtención de APIs, transformación, análisis y generación de reportes.**

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Prefect](https://img.shields.io/badge/Prefect-2.0+-green?style=for-the-badge&logo=prefect&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-Processing-orange?style=for-the-badge&logo=json&logoColor=white)

[![GitHub stars](https://img.shields.io/github/stars/RodrigoSamborms/CTF)](https://github.com/RodrigoSamborms/CTF/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/RodrigoSamborms/CTF)](https://github.com/RodrigoSamborms/CTF/issues)

</div>

---

## 📋 **Contenido**
- [🎯 Descripción](#-descripción)
- [✨ Características](#-características)
- [📦 Instalación](#-instalación)
- [🚀 Uso](#-uso)
- [📊 Archivos Generados](#-archivos-generados)
- [🛠️ Ejemplos](#️-ejemplos)
- [📝 Conclusiones](#-conclusiones)

## 🎯 **Descripción**

Este proyecto demuestra el poder de **Prefect** para crear pipelines de datos robustos y escalables. Utiliza la API de **JSONPlaceholder** para simular un escenario real de procesamiento de datos, incluyendo:

- **Obtención automática** de datos desde APIs externas
- **Procesamiento inteligente** con transformaciones y enriquecimiento
- **Manejo robusto de errores** con reintentos automáticos
- **Generación de reportes** en JSON y HTML
- **Logging profesional** para monitoreo y debugging

## ✨ **Características**

- **🔄 Reintentos Automáticos:** Manejo inteligente de fallos de red (3 reintentos con delay)
- **⚡ Procesamiento Paralelo:** Obtención simultánea de posts, usuarios y comentarios
- **📈 Análisis Avanzado:** Estadísticas, métricas y combinación de datos
- **💾 Almacenamiento Organizado:** Archivos JSON estructurados y reportes HTML
- **🔍 Logging Detallado:** Seguimiento completo de cada paso del pipeline
- **🎨 Reportes Visuales:** Dashboard HTML con estadísticas y gráficos
- **🛡️ Manejo de Errores:** Gestión robusta de excepciones y timeouts

## 📦 **Instalación**

```bash
# 1. Clonar el repositorio
git clone https://github.com/RodrigoSamborms/CTF.git
cd CTF/Practica04

# 2. Instalar dependencias
pip install prefect requests

# 3. Ejecutar el ejemplo
python prefect_json_example.py
```

## 🚀 **Uso**

### **Ejecución Simple**
```bash
python prefect_json_example.py
```

### **Monitoreo con Prefect UI**
```bash
# Iniciar servidor Prefect (opcional)
prefect server start

# En otra terminal, ejecutar con monitoreo
python prefect_json_example.py
```

## 📊 **Archivos Generados**

El pipeline genera automáticamente:

| Archivo | Descripción |
|---------|-------------|
| `json_data/posts_enriquecidos.json` | Posts con información de autor y estadísticas |
| `json_data/usuarios_procesados.json` | Información simplificada de usuarios |
| `json_data/estadisticas.json` | Métricas y análisis completo |
| `json_data/reporte_analisis.html` | Dashboard visual con gráficos |

## 🛠️ **Ejemplos**

### **Pipeline Básico**
```python
# Ejecutar pipeline completo
resultado = pipeline_jsonplaceholder()
print(f"Posts procesados: {resultado['estadisticas']['total_posts']}")
```

### **Tareas Individuales**
```python
# Obtener solo posts
posts = obtener_posts()

# Procesar datos específicos  
datos_procesados = procesar_posts(posts)
```

## 📝 **Conclusiones**

**Parte del uso de la IA no está en que realice el código por nosotros sino en que nos asiste en evitar tareas que son molestas, y que usualmente no forman parte del problema que se desea resolver.**

**PREFECT** nos asiste con los problemas de crear código que maneje las excepciones y problemas que pudieran presentarse en el manejo de datos entre funciones internas de nuestro código, es decir muchas de nuestras funciones usualmente son **Pipelines (tuberías)** cuya entrada de datos de una función son los resultados de otra, como el caso de pedir un dato al usuario donde tenemos que verificar que sean del tipo de datos esperados y no se ingresen cadenas por números.

Dichos datos usualmente deben ser formateados para poder ser procesados por otra función ya sea cuando debemos crear una tabla con varios valores numéricos y estos deben de normalizarse para presentar la misma cantidad de dígitos decimales y fraccionados. **Todas estas tareas no son parte del problema a resolver sino más bien requerimientos del código** que son necesarios para poder presentar los datos o manejarlos entre las funciones internas de nuestro código.

### **🎯 Aprendizajes Clave:**
- **🤖 IA como Asistente:** No reemplaza al programador, sino que elimina tareas tediosas
- **🔧 Prefect como Solución:** Maneja automáticamente excepciones y flujo de datos
- **⚡ Pipelines Eficientes:** Conexión fluida entre funciones con validación automática
- **🛡️ Robustez:** Manejo profesional de errores sin código adicional complejo

<div align="center">

---

### 🎯 **¡Dale una estrella si te gusta el proyecto!** ⭐

**Creado con ❤️ usando Prefect y Python**

</div>

