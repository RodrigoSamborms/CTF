"""
Ejemplo de Prefect con datos JSON de JSONPlaceholder
Este programa demuestra cómo usar Prefect para:
1. Obtener datos de JSONPlaceholder API
2. Procesar y transformar los datos
3. Guardar en archivos JSON locales
4. Generar reportes y análisis
"""

# PAQUETES NECESARIOS:
from prefect import task, flow
from prefect.logging import get_run_logger
import requests
import json
import os
from typing import List, Dict, Any
from datetime import datetime
import time

# Configuración 
BASE_URL = "https://jsonplaceholder.typicode.com"
DATA_DIR = "json_data"

@task
def crear_directorio_datos() -> str:
    """Crea el directorio para almacenar archivos JSON"""
    logger = get_run_logger()
    
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        logger.info(f"Directorio '{DATA_DIR}' creado")
    else:
        logger.info(f"Directorio '{DATA_DIR}' ya existe")
    
    return DATA_DIR

@task(retries=3, retry_delay_seconds=2)
def obtener_posts() -> List[Dict]:
    """Obtiene todos los posts de JSONPlaceholder"""
    logger = get_run_logger()
    
    try:
        logger.info("Obteniendo posts de JSONPlaceholder...")
        response = requests.get(f"{BASE_URL}/posts", timeout=10)
        response.raise_for_status()
        
        posts = response.json()
        logger.info(f"Obtenidos {len(posts)} posts exitosamente")
        
        return posts
    
    except requests.RequestException as e:
        logger.error(f"Error al obtener posts: {e}")
        raise

@task(retries=3, retry_delay_seconds=2)
def obtener_usuarios() -> List[Dict]:
    """Obtiene todos los usuarios de JSONPlaceholder"""
    logger = get_run_logger()
    
    try:
        logger.info("Obteniendo usuarios de JSONPlaceholder...")
        response = requests.get(f"{BASE_URL}/users", timeout=10)
        response.raise_for_status()
        
        usuarios = response.json()
        logger.info(f"Obtenidos {len(usuarios)} usuarios exitosamente")
        
        return usuarios
    
    except requests.RequestException as e:
        logger.error(f"Error al obtener usuarios: {e}")
        raise

@task(retries=3, retry_delay_seconds=2)
def obtener_comentarios() -> List[Dict]:
    """Obtiene todos los comentarios de JSONPlaceholder"""
    logger = get_run_logger()
    
    try:
        logger.info("Obteniendo comentarios de JSONPlaceholder...")
        response = requests.get(f"{BASE_URL}/comments", timeout=10)
        response.raise_for_status()
        
        comentarios = response.json()
        logger.info(f"Obtenidos {len(comentarios)} comentarios exitosamente")
        
        return comentarios
    
    except requests.RequestException as e:
        logger.error(f"Error al obtener comentarios: {e}")
        raise

@task
def procesar_posts(posts: List[Dict]) -> List[Dict]:
    """Procesa y enriquece la información de los posts"""
    logger = get_run_logger()
    logger.info("Procesando posts...")
    
    posts_procesados = []
    
    for post in posts:
        post_procesado = {
            "id": post["id"],
            "titulo": post["title"].title(),  # Capitalizar título
            "contenido": post["body"],
            "usuario_id": post["userId"],
            "longitud_titulo": len(post["title"]),
            "longitud_contenido": len(post["body"]),
            "palabras_titulo": len(post["title"].split()),
            "palabras_contenido": len(post["body"].split()),
            "fecha_procesamiento": datetime.now().isoformat()
        }
        posts_procesados.append(post_procesado)
    
    logger.info(f"Procesados {len(posts_procesados)} posts")
    return posts_procesados

@task
def procesar_usuarios(usuarios: List[Dict]) -> List[Dict]:
    """Procesa y simplifica la información de usuarios"""
    logger = get_run_logger()
    logger.info("Procesando usuarios...")
    
    usuarios_procesados = []
    
    for usuario in usuarios:
        usuario_procesado = {
            "id": usuario["id"],
            "nombre": usuario["name"],
            "username": usuario["username"],
            "email": usuario["email"],
            "telefono": usuario["phone"],
            "website": usuario["website"],
            "ciudad": usuario["address"]["city"],
            "codigo_postal": usuario["address"]["zipcode"],
            "empresa": usuario["company"]["name"],
            "fecha_procesamiento": datetime.now().isoformat()
        }
        usuarios_procesados.append(usuario_procesado)
    
    logger.info(f"Procesados {len(usuarios_procesados)} usuarios")
    return usuarios_procesados

@task
def combinar_datos(posts: List[Dict], usuarios: List[Dict], comentarios: List[Dict]) -> Dict[str, Any]:
    """Combina y analiza todos los datos obtenidos"""
    logger = get_run_logger()
    logger.info("Combinando y analizando datos...")
    
    # Crear un mapeo de usuarios por ID
    usuarios_map = {u["id"]: u for u in usuarios}
    
    # Contar comentarios por post
    comentarios_por_post = {}
    for comentario in comentarios:
        post_id = comentario["postId"]
        if post_id not in comentarios_por_post:
            comentarios_por_post[post_id] = 0
        comentarios_por_post[post_id] += 1
    
    # Enriquecer posts con información de usuario y comentarios
    posts_enriquecidos = []
    for post in posts:
        usuario = usuarios_map.get(post["usuario_id"], {})
        post_enriquecido = {
            **post,
            "autor_nombre": usuario.get("nombre", "Desconocido"),
            "autor_email": usuario.get("email", "N/A"),
            "autor_ciudad": usuario.get("ciudad", "N/A"),
            "total_comentarios": comentarios_por_post.get(post["id"], 0)
        }
        posts_enriquecidos.append(post_enriquecido)
    
    # Estadísticas generales
    estadisticas = {
        "total_posts": len(posts),
        "total_usuarios": len(usuarios),
        "total_comentarios": len(comentarios),
        "promedio_palabras_titulo": sum(p["palabras_titulo"] for p in posts) / len(posts),
        "promedio_palabras_contenido": sum(p["palabras_contenido"] for p in posts) / len(posts),
        "post_mas_comentado": max(posts_enriquecidos, key=lambda x: x["total_comentarios"]),
        "usuario_mas_activo": max(usuarios_map.values(), key=lambda x: len([p for p in posts if p["usuario_id"] == x["id"]])),
        "fecha_analisis": datetime.now().isoformat()
    }
    
    resultado = {
        "posts_enriquecidos": posts_enriquecidos,
        "usuarios": usuarios,
        "estadisticas": estadisticas
    }
    
    logger.info("Análisis de datos completado")
    return resultado

@task
def guardar_json(datos: Any, nombre_archivo: str, directorio: str) -> str:
    """Guarda datos en un archivo JSON"""
    logger = get_run_logger()
    
    ruta_archivo = os.path.join(directorio, nombre_archivo)
    
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as file:
            json.dump(datos, file, indent=2, ensure_ascii=False)
        
        logger.info(f"Archivo guardado exitosamente: {ruta_archivo}")
        return ruta_archivo
    
    except Exception as e:
        logger.error(f"Error al guardar archivo {ruta_archivo}: {e}")
        raise

@task
def generar_reporte_html(estadisticas: Dict, directorio: str) -> str:
    """Genera un reporte HTML con las estadísticas"""
    logger = get_run_logger()
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Reporte de Análisis JSONPlaceholder</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }}
            .container {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #333; border-bottom: 3px solid #4CAF50; padding-bottom: 10px; }}
            .stat {{ background: #e8f5e8; padding: 15px; margin: 10px 0; border-radius: 5px; }}
            .highlight {{ background: #fff3cd; padding: 10px; border-left: 4px solid #ffc107; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 Reporte de Análisis - JSONPlaceholder</h1>
            <p><strong>Fecha de análisis:</strong> {estadisticas['fecha_analisis']}</p>
            
            <h2>📈 Estadísticas Generales</h2>
            <div class="stat"><strong>Total de Posts:</strong> {estadisticas['total_posts']}</div>
            <div class="stat"><strong>Total de Usuarios:</strong> {estadisticas['total_usuarios']}</div>
            <div class="stat"><strong>Total de Comentarios:</strong> {estadisticas['total_comentarios']}</div>
            <div class="stat"><strong>Promedio de palabras en títulos:</strong> {estadisticas['promedio_palabras_titulo']:.1f}</div>
            <div class="stat"><strong>Promedio de palabras en contenido:</strong> {estadisticas['promedio_palabras_contenido']:.1f}</div>
            
            <h2>🏆 Destacados</h2>
            <div class="highlight">
                <strong>Post más comentado:</strong><br>
                "{estadisticas['post_mas_comentado']['titulo']}" 
                ({estadisticas['post_mas_comentado']['total_comentarios']} comentarios)
            </div>
            
            <div class="highlight">
                <strong>Usuario más activo:</strong><br>
                {estadisticas['usuario_mas_activo']['nombre']} 
                ({estadisticas['usuario_mas_activo']['email']})
            </div>
        </div>
    </body>
    </html>
    """
    
    ruta_reporte = os.path.join(directorio, "reporte_analisis.html")
    
    try:
        with open(ruta_reporte, 'w', encoding='utf-8') as file:
            file.write(html_content)
        
        logger.info(f"Reporte HTML generado: {ruta_reporte}")
        return ruta_reporte
    
    except Exception as e:
        logger.error(f"Error al generar reporte HTML: {e}")
        raise

# Flujo principal
@flow
def pipeline_jsonplaceholder():
    """
    Pipeline principal para procesar datos de JSONPlaceholder
    """
    logger = get_run_logger()
    logger.info("🚀 Iniciando pipeline de JSONPlaceholder")
    
    # Paso 1: Preparar directorio
    directorio = crear_directorio_datos()
    
    # Paso 2: Obtener datos (en paralelo)
    posts_raw = obtener_posts()
    usuarios_raw = obtener_usuarios()
    comentarios_raw = obtener_comentarios()
    
    # Paso 3: Procesar datos
    posts_procesados = procesar_posts(posts_raw)
    usuarios_procesados = procesar_usuarios(usuarios_raw)
    
    # Paso 4: Combinar y analizar
    datos_combinados = combinar_datos(posts_procesados, usuarios_procesados, comentarios_raw)
    
    # Paso 5: Guardar archivos JSON
    archivo_posts = guardar_json(
        datos_combinados["posts_enriquecidos"], 
        "posts_enriquecidos.json", 
        directorio
    )
    
    archivo_usuarios = guardar_json(
        datos_combinados["usuarios"], 
        "usuarios_procesados.json", 
        directorio
    )
    
    archivo_estadisticas = guardar_json(
        datos_combinados["estadisticas"], 
        "estadisticas.json", 
        directorio
    )
    
    # Paso 6: Generar reporte HTML
    reporte_html = generar_reporte_html(datos_combinados["estadisticas"], directorio)
    
    # Resultado final
    resultado = {
        "archivos_generados": [archivo_posts, archivo_usuarios, archivo_estadisticas, reporte_html],
        "estadisticas": datos_combinados["estadisticas"],
        "directorio_datos": directorio
    }
    
    logger.info("✅ Pipeline completado exitosamente")
    
    # Mostrar resumen
    print("\n" + "="*60)
    print("🎉 PIPELINE COMPLETADO EXITOSAMENTE")
    print("="*60)
    print(f"📁 Directorio de datos: {directorio}")
    print(f"📊 Posts procesados: {resultado['estadisticas']['total_posts']}")
    print(f"👥 Usuarios procesados: {resultado['estadisticas']['total_usuarios']}")
    print(f"💬 Comentarios analizados: {resultado['estadisticas']['total_comentarios']}")
    print(f"📄 Archivos generados: {len(resultado['archivos_generados'])}")
    print("\n📋 Archivos creados:")
    for archivo in resultado["archivos_generados"]:
        print(f"  • {archivo}")
    print("="*60)
    
    return resultado

if __name__ == "__main__":
    print("🔄 Ejecutando pipeline de JSONPlaceholder con Prefect...")
    resultado = pipeline_jsonplaceholder()