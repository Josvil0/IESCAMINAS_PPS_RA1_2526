# extractor_metadatos.py
# Aplicación para extraer metadatos de imágenes y documentos
# Uso: python extractor_metadatos.py ruta/al/archivo

import os
import sys
import json
import datetime
from PIL import Image, ExifTags
from PyPDF2 import PdfReader
from docx import Document


# =========================
# FUNCIONES DE METADATOS
# =========================

def obtener_metadatos_sistema(ruta):
    """
    Devuelve información básica del sistema de archivos:
    tamaño, fecha de creación y modificación.
    """
    estado = os.stat(ruta)
    return {
        "tamano_bytes": estado.st_size,
        "fecha_creacion": datetime.datetime.fromtimestamp(
            getattr(estado, "st_ctime")
        ).isoformat(),
        "fecha_modificacion": datetime.datetime.fromtimestamp(
            estado.st_mtime
        ).isoformat()
    }


def extraer_metadatos_imagen(ruta):
    """
    Extrae metadatos básicos de imágenes (JPG, PNG),
    filtrando solo los valores útiles de EXIF y evitando campos binarios problemáticos.
    """
    metadatos = {}
    try:
        # Usar 'with' asegura que el archivo se cierre automáticamente
        with Image.open(ruta) as imagen:
            metadatos["formato"] = imagen.format
            metadatos["tamano"] = f"{imagen.size[0]}x{imagen.size[1]}"
            metadatos["modo_color"] = imagen.mode

            # EXIF si existe
            if hasattr(imagen, "_getexif") and imagen._getexif():
                exif_legible = {}
                ignorar_campos = {"MakerNote", "UserComment", "ThumbnailImage"}  # campos problemáticos
                for id_etiqueta, valor in imagen._getexif().items():
                    etiqueta = ExifTags.TAGS.get(id_etiqueta, id_etiqueta)
                    
                    if etiqueta in ignorar_campos:
                        continue  # ignorar campos que generan basura

                    # Solo valores simples: int, float, str
                    if isinstance(valor, (int, float, str)):
                        exif_legible[str(etiqueta)] = valor
                    # Intentar decodificar bytes a texto legible
                    elif isinstance(valor, bytes):
                        try:
                            valor_decodificado = valor.decode(errors="ignore").strip()
                            if valor_decodificado:
                                exif_legible[str(etiqueta)] = valor_decodificado
                        except Exception:
                            continue
                    # Ignorar tuplas, listas, etc.
                    else:
                        continue

                if exif_legible:
                    metadatos["exif"] = exif_legible

    except Exception as error:
        metadatos["error"] = f"Error al leer la imagen: {error}"

    return metadatos


def extraer_metadatos_pdf(ruta):
    """
    Extrae metadatos básicos de archivos PDF.
    """
    metadatos = {}
    try:
        lector = PdfReader(ruta)
        info = lector.metadata
        if info:
            for clave, valor in info.items():
                if valor is not None:
                    metadatos[str(clave)] = str(valor)
    except Exception as error:
        metadatos["error"] = f"Error al leer el PDF: {error}"

    return metadatos


def extraer_metadatos_docx(ruta):
    """
    Extrae propiedades de documentos DOCX.
    """
    metadatos = {}
    try:
        documento = Document(ruta)
        propiedades = documento.core_properties

        if propiedades.author:
            metadatos["autor"] = propiedades.author
        if propiedades.title:
            metadatos["titulo"] = propiedades.title
        if propiedades.created:
            metadatos["fecha_creacion"] = propiedades.created.isoformat()
        if propiedades.modified:
            metadatos["fecha_modificacion"] = propiedades.modified.isoformat()

    except Exception as error:
        metadatos["error"] = f"Error al leer el DOCX: {error}"

    return metadatos


def extraer_metadatos(ruta):
    """
    Función principal que detecta el tipo de archivo y extrae metadatos.
    """
    if not os.path.exists(ruta):
        raise FileNotFoundError("El archivo no existe")

    _, extension = os.path.splitext(ruta.lower())

    resultado = {
        "sistema_archivos": obtener_metadatos_sistema(ruta)
    }

    if extension in [".jpg", ".jpeg", ".png"]:
        resultado["imagen"] = extraer_metadatos_imagen(ruta)
    elif extension == ".pdf":
        resultado["pdf"] = extraer_metadatos_pdf(ruta)
    elif extension == ".docx":
        resultado["docx"] = extraer_metadatos_docx(ruta)
    else:
        resultado["nota"] = f"No hay extractor para archivos '{extension}'"

    return resultado


# =========================
# EJECUCIÓN POR TERMINAL
# =========================

def main():
    if len(sys.argv) != 2:
        print("Uso: python extractor_metadatos.py ruta/al/archivo")
        sys.exit(1)

    ruta = sys.argv[1]

    try:
        metadatos = extraer_metadatos(ruta)
        print("\nMetadatos extraídos:\n")
        print(json.dumps(metadatos, indent=2, ensure_ascii=False))

    except FileNotFoundError as error:
        print("Error:", error)
    except Exception as error:
        print("Error inesperado:", error)


if __name__ == "__main__":
    main()
