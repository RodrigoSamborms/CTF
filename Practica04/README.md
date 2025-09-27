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

<div align="center">

---

### 🎯 **¡Dale una estrella si te gusta el proyecto!** ⭐

**Creado con ❤️ usando Prefect y Python**

</div>