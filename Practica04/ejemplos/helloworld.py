from prefect import task, flow
from prefect.logging import get_run_logger
from typing import List
import time
import random

# Ejemplo básico - Tu código original
@task
def saludo_tarea() -> str:
    logger = get_run_logger()
    logger.info("Ejecutando tarea de saludo")
    print("Hola Mundo!")
    return "Hola Prefect"

@flow
def mi_flujo_hello_world(s: str):
    logger = get_run_logger()
    logger.info(f"Ejecutando flujo con mensaje: {s}")
    print(s)

# Ejemplo más avanzado con múltiples tareas
@task
def extraer_datos(fuente: str) -> List[dict]:
    """Simula la extracción de datos de una fuente"""
    logger = get_run_logger()
    logger.info(f"Extrayendo datos de {fuente}")
    
    # Simular tiempo de extracción
    time.sleep(1)
    
    # Datos de ejemplo
    datos = [
        {"id": i, "nombre": f"Usuario_{i}", "valor": random.randint(1, 100)}
        for i in range(1, 6)
    ]
    
    logger.info(f"Extraídos {len(datos)} registros")
    return datos

@task
def procesar_datos(datos: List[dict]) -> List[dict]:
    """Procesa y transforma los datos"""
    logger = get_run_logger()
    logger.info("Procesando datos...")
    
    datos_procesados = []
    for item in datos:
        item_procesado = {
            "id": item["id"],
            "nombre": item["nombre"].upper(),
            "valor": item["valor"] * 2,  # Duplicar el valor
            "categoria": "ALTO" if item["valor"] > 50 else "BAJO"
        }
        datos_procesados.append(item_procesado)
    
    logger.info(f"Procesados {len(datos_procesados)} registros")
    return datos_procesados

@task
def guardar_datos(datos: List[dict], destino: str) -> int:
    """Simula guardar datos en un destino"""
    logger = get_run_logger()
    logger.info(f"Guardando {len(datos)} registros en {destino}")
    
    # Simular tiempo de guardado
    time.sleep(0.5)
    
    # Simular guardado exitoso
    registros_guardados = len(datos)
    logger.info(f"Guardados exitosamente {registros_guardados} registros")
    
    return registros_guardados

@task
def generar_reporte(total_registros: int) -> str:
    """Genera un reporte resumen"""
    logger = get_run_logger()
    reporte = f"Reporte de procesamiento:\n- Total de registros procesados: {total_registros}\n- Estado: Exitoso"
    logger.info("Reporte generado exitosamente")
    return reporte

# Flujo principal que orquesta todas las tareas
@flow
def pipeline_datos(fuente: str = "API", destino: str = "base_datos"):
    """Pipeline principal de procesamiento de datos"""
    logger = get_run_logger()
    logger.info("Iniciando pipeline de datos")
    
    # Ejecutar tareas en secuencia
    datos_raw = extraer_datos(fuente)
    datos_procesados = procesar_datos(datos_raw)
    total_guardados = guardar_datos(datos_procesados, destino)
    reporte = generar_reporte(total_guardados)
    
    logger.info("Pipeline completado exitosamente")
    print(reporte)
    
    return {
        "registros_procesados": total_guardados,
        "reporte": reporte
    }

# Ejemplo con tareas paralelas
@task
def tarea_paralela_1(nombre: str) -> str:
    logger = get_run_logger()
    logger.info(f"Ejecutando tarea paralela 1 - {nombre}")
    time.sleep(2)
    return f"Resultado de {nombre} - Tarea 1"

@task
def tarea_paralela_2(nombre: str) -> str:
    logger = get_run_logger()
    logger.info(f"Ejecutando tarea paralela 2 - {nombre}")
    time.sleep(1.5)
    return f"Resultado de {nombre} - Tarea 2"

@task
def combinar_resultados(resultado1: str, resultado2: str) -> str:
    logger = get_run_logger()
    logger.info("Combinando resultados de tareas paralelas")
    return f"Combinado: {resultado1} + {resultado2}"

@flow
def flujo_paralelo(nombre_proyecto: str = "Proyecto Demo"):
    """Ejemplo de flujo con tareas que se ejecutan en paralelo"""
    logger = get_run_logger()
    logger.info(f"Iniciando flujo paralelo para {nombre_proyecto}")
    
    # Estas tareas se ejecutarán en paralelo
    resultado1 = tarea_paralela_1(nombre_proyecto)
    resultado2 = tarea_paralela_2(nombre_proyecto)
    
    # Esta tarea esperará a que terminen las anteriores
    resultado_final = combinar_resultados(resultado1, resultado2)
    
    logger.info("Flujo paralelo completado")
    print(resultado_final)
    
    return resultado_final

if __name__ == "__main__":
    print("=== Ejemplo 1: Hello World Básico ===")
    r = saludo_tarea()
    mi_flujo_hello_world(r)
    
    print("\n=== Ejemplo 2: Pipeline de Datos ===")
    resultado_pipeline = pipeline_datos()
    
    print("\n=== Ejemplo 3: Tareas Paralelas ===")
    resultado_paralelo = flujo_paralelo()
    
    print("\n=== Todos los ejemplos completados ===")
    print(f"Pipeline procesó {resultado_pipeline['registros_procesados']} registros")
    print(f"Flujo paralelo: {resultado_paralelo}")