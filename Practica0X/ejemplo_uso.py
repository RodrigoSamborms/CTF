"""
Ejemplo de uso del Analizador Multi-Documento
============================================

Este script demuestra cómo usar el analizador para procesar
archivos PDF, DOC y código fuente automáticamente.
"""

from multi_document_analyzer import DocumentAnalyzer
import os

def ejemplo_analisis_completo():
    """Ejemplo completo de análisis multi-documento"""
    
    print("🔍 Iniciando Análisis Multi-Documento")
    print("="*50)
    
    # Crear instancia del analizador
    analyzer = DocumentAnalyzer()
    
    # Lista de archivos a analizar (ajusta según tus archivos)
    archivos_a_analizar = []
    
    # Buscar archivos automáticamente en el directorio actual
    directorio_actual = os.getcwd()
    
    for archivo in os.listdir(directorio_actual):
        extension = os.path.splitext(archivo)[1].lower()
        
        # Agregar archivos soportados
        if extension in ['.pdf', '.docx', '.doc', '.py', '.js', '.ts', 
                        '.java', '.cpp', '.c', '.cs', '.php', '.rb', '.go']:
            # Evitar analizar el propio script analizador
            if archivo not in ['multi_document_analyzer.py', 'ejemplo_uso.py']:
                archivos_a_analizar.append(archivo)
    
    if not archivos_a_analizar:
        print("⚠️  No se encontraron archivos para analizar en el directorio actual")
        print("\nArchivos soportados:")
        print("- PDF: .pdf")
        print("- Documentos: .docx, .doc") 
        print("- Código: .py, .js, .ts, .java, .cpp, .c, .cs, .php, .rb, .go")
        return
    
    print(f"📁 Archivos encontrados para análisis: {len(archivos_a_analizar)}")
    for archivo in archivos_a_analizar:
        print(f"  ✓ {archivo}")
    
    print("\n🚀 Iniciando procesamiento...")
    
    # Procesar todos los archivos
    readme_generado = analyzer.procesar_multiples_archivos(archivos_a_analizar)
    
    print(f"\n✅ Análisis completado!")
    print(f"📄 README generado: {readme_generado}")
    print(f"📊 Datos detallados: analisis_completo.json")

def ejemplo_archivo_especifico():
    """Ejemplo para analizar archivos específicos"""
    
    # Archivos específicos que quieres analizar
    archivos_especificos = [
        "INSTALACIÓN DE AIRFLOW EN LA RASPBERRY PI 3.pdf",  # PDF existente
        "prefect_json_example.py"  # Si existe en el directorio padre
    ]
    
    analyzer = DocumentAnalyzer()
    
    # Verificar cuáles archivos existen
    archivos_existentes = []
    for archivo in archivos_especificos:
        if os.path.exists(archivo):
            archivos_existentes.append(archivo)
        else:
            print(f"⚠️  Archivo no encontrado: {archivo}")
    
    if archivos_existentes:
        print(f"📁 Analizando {len(archivos_existentes)} archivos específicos...")
        readme_generado = analyzer.procesar_multiples_archivos(archivos_existentes)
        print(f"✅ README generado: {readme_generado}")
    else:
        print("❌ No se encontraron archivos para analizar")

def instalar_dependencias():
    """Instala las dependencias necesarias"""
    import subprocess
    import sys
    
    dependencias = ["PyMuPDF", "python-docx"]
    
    print("📦 Instalando dependencias necesarias...")
    
    for dep in dependencias:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
            print(f"✅ {dep} instalado correctamente")
        except subprocess.CalledProcessError:
            print(f"❌ Error instalando {dep}")

if __name__ == "__main__":
    print("🔍 Analizador Multi-Documento - Ejemplo de Uso")
    print("=" * 60)
    
    # Preguntar qué tipo de análisis hacer
    print("\nOpciones disponibles:")
    print("1. Análisis automático (buscar archivos en directorio actual)")
    print("2. Análisis de archivos específicos")
    print("3. Instalar dependencias")
    
    opcion = input("\nSelecciona una opción (1-3): ").strip()
    
    if opcion == "1":
        ejemplo_analisis_completo()
    elif opcion == "2":
        ejemplo_archivo_especifico()
    elif opcion == "3":
        instalar_dependencias()
    else:
        print("❌ Opción no válida")
        
    print("\n🎉 ¡Gracias por usar el Analizador Multi-Documento!")